//
// Created by mikaa on 17-12-29.
//

#include <can/CanNode.h>

namespace PIAUTO {
    namespace chassis {
        int CanNode::logFileCount = 0;

        string CanNode::FRAME_RECORD_PATH = "../frameRecord";

        CanNode::CanNode(const string &file_name) {
            if (!logFile.is_open()) {
                logFile.open((FRAME_RECORD_PATH + "/" + file_name).c_str(),
                             std::ios::in | std::ios::out | std::ios::trunc);
            }
            ++logFileCount;
        }

        CanNode::~CanNode() {
            if (--logFileCount == 0)
                logFile.close();
        }
    }
}
