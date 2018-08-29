//
// Created by mikaa on 17-12-28.
//

#include <ctime>
#include <sys/time.h>

#include <utils/PITime.h>

namespace PIAUTO {
    namespace time {
        uint64_t GetCurrentTimeMilliSec() {
            struct timespec t;
            clock_gettime(CLOCK_MONOTONIC, &t);
            uint64_t cur_milli_sec =
                    (uint64_t) ((uint64_t) t.tv_nsec / 1000000 + (((uint64_t) t.tv_sec) * 1000));
            return cur_milli_sec;
        }

        uint64_t getCurrentTicks() {
            timeval t;
            gettimeofday(&t, NULL);
            return static_cast<uint64_t>(t.tv_sec) * 1000ull +
                   static_cast<uint64_t>(t.tv_usec / 1000);
        }

        std::string getTimeStamps() {
            struct timeval now_time;
            gettimeofday(&now_time, NULL);
            time_t tt = now_time.tv_sec;
            tm *temp = localtime(&tt);
            char time_str[100] = {0};
            sprintf(time_str, "%04d-%02d-%02d %02d:%02d:%02d.%ld",
                    temp->tm_year + 1900, temp->tm_mon + 1, temp->tm_mday, temp->tm_hour, temp->tm_min, temp->tm_sec,
                    now_time.tv_usec);
            return time_str;
        }
    }
}
