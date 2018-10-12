//
// Created by mikaa on 17-12-4.
//

#include <sensor/UltraSonicRadar.h>

namespace PIAUTO {
    namespace chassis {
        std::ostream &operator<<(std::ostream &os, const SonarData &sonar_data) {
            os << "left_front: "<< sonar_data.left_front
               << " right_front: " << sonar_data.right_front;
            return os;
        }

        UltraSonicRadar::UltraSonicRadar(CanTransmitter *c) : CanNode("sonar.txt"), ct(c), sonar_buffer(DEFAULT_SONAR_BUFFER_SIZE) {
            attri = new USRadarAttributes();
        }

        UltraSonicRadar::~UltraSonicRadar() {
            delete attri;
        }

        bool UltraSonicRadar::UpdateAttributes(VCI_CAN_OBJ &frame) {
            #if DEBUG
            std::thread::id update_attributes_id = std::this_thread::get_id();
            cout << "[" << __func__ << "] in thread(" << update_attributes_id << ")     0x" << std::hex << frame.ID << endl;
            #endif

            int tail_index = -1;
            for (int i = 0; i != 4; i++) {
                if (frame.ID == static_cast<unsigned int>(0x790 + i)) {
                    tail_index = i;
                    break;
                }
            }
            if (-1 == tail_index) {
                return false;
            }

            int index = frame.Data[0] + tail_index * 2 - 5;
            printf("func: %s, line: %d, frame.Data[0]: %d, tail_index: %d, index: %d\n", __func__, __LINE__, frame.Data[0], tail_index, index);
            #if DEBUG
            cout << Frame2Str(frame).c_str()<<"\n";
            #endif
            // logFile<< Frame2Str(frame).c_str()<<"\n";
            attri->Timer_800[index].Reset();
            // lock data
            std::unique_lock<std::shared_timed_mutex> lg(_mt);
            memcpy(&attri->_800[index], frame.Data, 8);

            if (index == 0) {
                #if DEBUG
                printf("index is 0!\n");
                #endif

                SonarData objs = {
                    ReverseHLValue(attri->_800[0].Range),
                    ReverseHLValue(attri->_800[1].Range),
                    ReverseHLValue(attri->_800[7].Range),
                    ReverseHLValue(attri->_800[2].Range),
                    ReverseHLValue(attri->_800[6].Range),
                    ReverseHLValue(attri->_800[3].Range),
                    ReverseHLValue(attri->_800[5].Range),
                    ReverseHLValue(attri->_800[4].Range),
                };
                sonar_buffer.Push(objs);
            }
            return true;
        }

        bool UltraSonicRadar::VerifyFrameTimer() {
            bool ret = true;
            for (int i = 0; i < USRADAR_NUM; i++) {
                if (attri->Timer_800[i].GetTime() > TIME_INTERVAL_800) {
                    #if DEBUG
                    cout << "sonar " << i << ": Frame_800 receive overtime! " << attri->Timer_800[i].GetTime() << endl;
                    #endif
                    LOG(ERROR) << "sonar " << i << ": Frame_800 receive overtime! " << attri->Timer_800[i].GetTime() << endl;
                    ret = false;
                }
            }
            return ret;
        }

        bool UltraSonicRadar::GetObjectInfoByTimes(SonarData *_buff, int len) {
            std::shared_lock<std::shared_timed_mutex> lg(_mt);
            return sonar_buffer.GetData(_buff, len);
        };
    }
}
