//
// Created by mikaa on 17-12-4.
//

#include <sensor/Radar77.h>

namespace PIAUTO {
    namespace chassis {
        std::ostream &operator<<(std::ostream &os, const ObjectInfo_77 &obj) {
            os << "index: "<<obj.index
               << " distance: " << obj.Range
               << " RadialVelocity: " << obj.RadialVelocity
               << " RadialAcc: " << obj.RadialAcc
               << " Angle: " << obj.Azimuth
               << " Power: " << obj.Power;
            return os;
        }

        Radar_77::Radar_77(int id, CanTransmitter *c) : CanNode("radar.txt"), ID(id), ct(c), objs(64), radar_buffer(20) {
            attri = new Radar_77Attributes();
        }

        Radar_77::~Radar_77() {
            delete attri;
        }

        bool Radar_77::UpdateAttributes(VCI_CAN_OBJ &frame) {
            std::thread::id update_attributes_id = std::this_thread::get_id();
            cout << "[" << __func__ << "] in thread(" << update_attributes_id << ")     0x" << std::hex << frame.ID << endl;
            if (frame.ID < static_cast<unsigned int>(0x500 + 0x40 *ID) || frame.ID > static_cast<unsigned int>(0x500 + 0x40 *ID + 0x3f)) {
                return false;
            }

            obj_index = frame.ID - 0x500 - 0x40 *ID;

            cout << Frame2Str(frame).c_str()<<"\n";
            // logFile<< Frame2Str(frame).c_str()<<"\n";
            memcpy(&attri->_500[obj_index], frame.Data, 8);

            if (obj_index == 63) {
                printf("obj_index is 63!\n");
                std::unique_lock<std::shared_timed_mutex> lg(_mt);
                /// all frame received, notify observers
                objs.clear();
                attri->Timer_500.Reset();
                uint16_t templeData;

                ObjectInfo_77 temp;
                for (int i = 0; i < 63; ++i) {
                    if(attri->_500[i].Range == 0)
                        continue;
                    printf("i: %d\n", i);
                    temp.index=i;

                    temp.Range = attri->_500[i].Range * 0.01;

                    templeData = attri->_500[i].RadialVelocity;
                    temp.RadialVelocity = (templeData > 8191 ? (templeData - 16384)*0.01f : templeData*0.01f);

                    templeData = attri->_500[i].RadialAcc;
                    temp.RadialAcc = (templeData > 511 ? (templeData - 1024)*0.05f : templeData*0.05f);

                    templeData = attri->_500[i].Angle;
                    temp.Azimuth = (templeData > 1023 ? (templeData- 2048) *0.1f : templeData *0.1f);

                    templeData = attri->_500[i].Power;
                    temp.Power = (templeData > 511 ? (templeData - 1024)*0.1f - 40 : templeData*0.1f - 40);

                    objs.push_back(temp);
                    memset(&attri->_500[i],0,8);
                }
                radar_buffer.Push(objs);

                obj_index=0;
            }
            return true;
        }

        bool Radar_77::VerifyFrameTimer() {
            if (attri->Timer_500.GetTime() > TIME_INTERVAL_500) {
                LOG(ERROR) << "radar " << ID << ": Frame_500 receive overtime! " << attri->Timer_500.GetTime() << endl;
                return false;
            }
            return true;
        }

        std::vector<ObjectInfo_77> Radar_77::GetObjectInfo() {
            std::shared_lock<std::shared_timed_mutex> lg(_mt);
            return objs;
        }

        bool Radar_77::GetObjectInfoByTimes(std::vector<ObjectInfo_77> *_buff, int len) {
            std::shared_lock<std::shared_timed_mutex> lg(_mt);
            return radar_buffer.GetData(_buff, len);
        };
    }
}
