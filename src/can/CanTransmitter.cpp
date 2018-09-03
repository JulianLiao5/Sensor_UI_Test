
#include <sys/stat.h>
#include <can/CanTransmitter.h>
#include <sensor/Radar77.h>

namespace PIAUTO {
    namespace chassis {
        CanTransmitter::CanTransmitter(
                DWORD dt,
                DWORD idx,
                DWORD cn,
                DWORD code,
                DWORD mask,
                UCHAR filterType,
                UCHAR mode,
                UCHAR timing0,
                UCHAR timing1
        ) : devtype(dt), index(idx), cannum(cn) {

            auto oldmask = umask(0);
            mkdir(LOGPATH, 0777);
            umask(oldmask);

            google::InitGoogleLogging("PI_AUTO"); //initiate glog
            FLAGS_log_dir = LOGPATH;


            if (VCI_OpenDevice(devtype, index, 0) != STATUS_OK) {
                LOG(ERROR) << "Failed to open device!";
                exit(1);
            }

            Init(code, mask, filterType, mode, timing0, timing1);

            m_connect = true;

            ReceiveThread = new thread(&CanTransmitter::ReceiveData, this);

            usleep(5 * 1000);
            monitor_Thread = new thread(&CanTransmitter::FrameRateMonitor, this);
        }

        CanTransmitter::~CanTransmitter() {
            m_connect = false;
            ReceiveThread->join();
            delete ReceiveThread;
            if (VCI_CloseDevice(devtype, index) == STATUS_ERR)
                cout << "Close device error!" << endl;
            monitor_Thread->join();
            delete monitor_Thread;
            google::ShutdownGoogleLogging();
        }

        void CanTransmitter::Init(
                DWORD code,
                DWORD mask,
                UCHAR filterType,
                UCHAR mode,
                UCHAR timing0,
                UCHAR timing1
        ) {
            VCI_INIT_CONFIG init_config;
            init_config.AccCode = code == 0 ? 0 : code;
            init_config.AccMask = mask == 0 ? 0xffffffff : mask;
            init_config.Filter = filterType == 0 ? (UCHAR) 0 : filterType;
            init_config.Mode = mode == 0 ? (UCHAR) 0 : mode;
            init_config.Timing0 = timing0 == 0 ? (UCHAR) 0 : timing0;
            init_config.Timing1 = timing1 == 0 ? (UCHAR) 0x1c : timing1;

            if (VCI_InitCAN(devtype, index, cannum, &init_config) != STATUS_OK) {
                LOG(ERROR) << "Failed to initialize the CAN!";
                exit(1);
            }

            if (VCI_StartCAN(devtype, index, cannum) != STATUS_OK) {
                LOG(ERROR) << "Failed to start";
                exit(1);
            }
            LOG(INFO) << "Start successfully";
        }

        VCI_CAN_OBJ CanTransmitter::
        GenerateFrame(const string &ID, const string &Data, BYTE SendType, BYTE ExternFlag, BYTE RomoteFlag) {
            VCI_CAN_OBJ vciCanObj{0};
            char szFrameID[9];
            unsigned char FrameID[4] = {0, 0, 0, 0};
            memset(szFrameID, '0', 9);
            unsigned char FrameData[8];
            char szData[25];
            BYTE len = 0;


            if (ID.empty() ||
                (Data.empty() && ExternFlag == 0)) {
                LOG(ERROR) << "Please enter the data";
                return vciCanObj;
            }

            if (ID.size() > 8) {
                LOG(ERROR) << "ID-value out of range";
                return vciCanObj;
            }
            if (Data.size() > 24) {
                LOG(ERROR) << "Data longer than the range maximum is 8 bytes";
                return vciCanObj;
            }
            if (ExternFlag == 0) {
                if (Data.size() % 3 == 1) {
                    LOG(ERROR) << "Data format is wrong, please re-enter";
                    return vciCanObj;
                }
            }
            memcpy(&szFrameID[8 - ID.size()], ID.c_str(), ID.size());
            StrToData((unsigned char *) szFrameID, FrameID, 4, 0);

            len = static_cast<unsigned char>((Data.size() + 1) / 3);
            strcpy(szData, Data.c_str());

            StrToData((unsigned char *) szData, FrameData, len, 1);

            vciCanObj.DataLen = len;

            memcpy(&vciCanObj.Data, FrameData, len);

            vciCanObj.SendType = SendType;
            vciCanObj.RemoteFlag = RomoteFlag;
            vciCanObj.ExternFlag = ExternFlag;

            if (vciCanObj.ExternFlag == 1) {
                vciCanObj.ID = ((DWORD) FrameID[0] << 24) + ((DWORD) FrameID[1] << 16) + ((DWORD) FrameID[2] << 8) +
                               ((DWORD) FrameID[3]);
            } else {
                vciCanObj.ID = ((DWORD) FrameID[2] << 8) + ((DWORD) FrameID[3]);
            }
            return vciCanObj;
        }

        void CanTransmitter::GenerateChecksum(VCI_CAN_OBJ *frame) {
            for (int i = 0; i != 7; ++i)
                frame->Data[7] ^= frame->Data[i];
        }


        bool CanTransmitter::SendData(VCI_CAN_OBJ *frame) {
            int ret = 0;

            std::unique_lock<std::mutex> lg(_mt);
            ret = VCI_Transmit(devtype, index, cannum, frame, 1);
            lg.unlock();

            if (ret != STATUS_OK) {
                cout << "send command though CanBus failed!" << endl;
                LOG(ERROR) << "SendData failed " << Frame2Str(*frame);
                VCI_ERR_INFO errInfo;
                VCI_ReadErrInfo(devtype, index, cannum, &errInfo);
                LOG(ERROR) << "SendData error, ErrCode=" << std::hex << errInfo.ErrCode
                           << " PassiveErrData=" << (UINT) errInfo.Passive_ErrData[0]
                           << (UINT) errInfo.Passive_ErrData[1] << (UINT) errInfo.Passive_ErrData[2]
                           << " ArLostErrData=" << (UINT) errInfo.ArLost_ErrData;
                /*throw exception code*/
                //--------------------------------------------------
            } else {
                sendFrameNum += ret;
            }

            return ret;
        }

        void CanTransmitter::ReceiveData() {
            std::thread::id receive_data_id = std::this_thread::get_id();
            cout << "ReceiveData thread(" << receive_data_id << ") begin!" << endl;
            VCI_CAN_OBJ vciCanObj[100];
            VCI_ERR_INFO errInfo{0};
            ULONG len;
            UINT buffLen = 0;
            while (m_connect) {
                buffLen = VCI_GetReceiveNum(devtype, index, cannum);
                printf("[%s], buffLen: %d\n", __func__, buffLen);
                if (buffLen != 0) {
                    buffLen = std::min(buffLen, 100U);
                    len = VCI_Receive(devtype, index, cannum, vciCanObj, buffLen, 100);
                    if (len == 0xFFFFFFFF) {
                        printf("len ERROR!\n");
                        VCI_ReadErrInfo(devtype, index, cannum, &errInfo);
                        LOG(ERROR) << "ReceiveData error, ErrCode=" << std::hex << errInfo.ErrCode
                                   << " PassiveErrData=" << (UINT) errInfo.Passive_ErrData[0]
                                   << (UINT) errInfo.Passive_ErrData[1] << (UINT) errInfo.Passive_ErrData[2]
                                   << " ArLostErrData=" << (UINT) errInfo.ArLost_ErrData;
                        /*throw exception code*/
                        //-------------------------------------------

                        VCI_CAN_OBJ can;
                        can = GenerateFrame("0051", "00 01 00 00 00 00 00 00 ");
                        SendData(&can);
                    } else {
                        recvFrameNum += len;
                        printf("[%s], len: %d\n", __func__, len);
                        std::unique_lock<std::mutex> parsesLock(mutexParses);
                        for (unsigned int i = 0; i < len; i++) {
                            for (CanParse parse : *(parses_)) {
                              parse(vciCanObj[i]);
                            }
                        }
                        parsesLock.unlock();
                    }
                } else {
                    usleep(5 * 1000);
                }
            }
            cout << "Receive Thread Exit" << endl;
        }


        void CanTransmitter::registerCallbacks(CanParse &parse) {
          std::unique_lock<std::mutex> parsesLock(mutexParses);
          parses_->push_back(parse);
          parsesLock.unlock();
        }

        void CanTransmitter::unregisterCallbacks(unsigned int &index) {
            std::unique_lock<std::mutex> parsesLock(mutexParses);
            if (parses_->size() > 0 && index < parses_->size()) {
              parses_->erase(parses_->begin() + index);
            }
            parsesLock.unlock();
        }

        //Tools functions
        string Frame2Str(VCI_CAN_OBJ &frame) {
            string str;
            char tmpstr[50];
            if (frame.TimeFlag == 0)
                sprintf(tmpstr, "Time stamps:null");
            else
                sprintf(tmpstr, "Time stamps:%08x ", frame.TimeStamp);
            str += tmpstr;
            sprintf(tmpstr, "ID:%08x ", frame.ID);
            str += tmpstr;
            str += "Type:";
            if (frame.RemoteFlag == 0)
                sprintf(tmpstr, "Data frame ");
            else
                sprintf(tmpstr, "Remote frame ");
            str += tmpstr;
            str += "Format:";
            if (frame.ExternFlag == 0)
                sprintf(tmpstr, "Standard frame ");
            else
                sprintf(tmpstr, "Extended frame ");
            str += tmpstr;
            str += "\n";
            //cout << str << endl;
            //box->InsertString(box->GetCount(), str);
            if (frame.RemoteFlag == 0) {
                str += "Data:";
                if (frame.DataLen > 8)
                    frame.DataLen = 8;
                for (int j = 0; j < frame.DataLen; j++) {
                    sprintf(tmpstr, "%02x ", frame.Data[j]);
                    str += tmpstr;
                }
            }
            return str;
        }

        void recordFrame(std::fstream &file, VCI_CAN_OBJ &frame) {
            file << time::getCurrentTicks() << " " << frame.ID << " " << (long long *) frame.Data << "\n";
        }

        bool CharToInt(unsigned char chr, unsigned char *cint) {
            unsigned char cTmp;
            cTmp = static_cast<unsigned char>(chr - 48);
            if (cTmp >= 0 && cTmp <= 9) {
                *cint = cTmp;
                return true;
            }
            cTmp = static_cast<unsigned char>(chr - 65);
            if (cTmp >= 0 && cTmp <= 5) {
                *cint = static_cast<unsigned char>(cTmp + 10);
                return true;
            }
            cTmp = static_cast<unsigned char>(chr - 97);
            if (cTmp >= 0 && cTmp <= 5) {
                *cint = static_cast<unsigned char>(cTmp + 10);
                return true;
            }
            return false;
        }

        bool StrToData(unsigned char *str, unsigned char *data, int len, int flag) {
            unsigned char cTmp = 0;
            for (int j = 0; j < len; j++) {
                if (str == nullptr || !CharToInt(*str++, &cTmp))
                    return false;
                data[j] = cTmp;
                if (str == nullptr || !CharToInt(*str++, &cTmp))
                    return false;
                data[j] = (data[j] << 4) + cTmp;
                if (flag == 1)
                    ++str;
            }
            return true;
        }

        void InsertDataOnBytes(BYTE *raw, int val, int begin, int length) {
            for (int i = 0; i != length; ++i) {
                raw[begin++] = (BYTE) val;
                val >>= 8;
            }
        }

        bool VerifyFrame(VCI_CAN_OBJ *frame) {
            BYTE temp = 0;
            for (int i = 0; i != 7; ++i)
                temp ^= frame->Data[i];
            return temp == frame->Data[7];
        }

        unsigned short ReverseHLValue(unsigned short val) {
            unsigned short ret = val;
            ret <<= 8;
            val >>= 8;
            return ret + val;
        }
    }
}
