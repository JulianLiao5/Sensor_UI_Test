/*************************************************************************
	> File Name: test_ogm.cpp
	> Author: 
	> Mail: 
	> Created Time: 2018年08月28日 星期二 14时41分45秒
 ************************************************************************/

#include<functional>
#include <math.h>
#include<iostream>
#include<fstream>
#include <opencv2/core.hpp>
#include <opencv2/highgui.hpp>

#include <utils/sensor_coordinate.h>
#include <utils/occupancy_status_grid_map.h>

using namespace std;

#define TIME_0    0x00
#define TIME_1    0x1C

ofstream leftRadarFile;
ofstream middleRadarFile;
ofstream rightRadarFile;
ofstream overallRadarFile;
void logToFile(int index, PIAUTO::chassis::ObjectInfo_77 &object_info);

int main(int argc, char *argv[]) {
  PIAUTO::chassis::Radar_77 *radars[RADAR77_NUM];
  // for the third parameter, if radar connects to "CAN1", then it is 0; if radar connects to "CAN2", then it is 1;
  PIAUTO::chassis::CanTransmitter ct(VCI_USBCAN2, 0, 0, 0, 0, 0, 0, TIME_0, TIME_1);
  for (int i = 0; i < RADAR77_NUM; i++) {
      radars[i] = new PIAUTO::chassis::Radar_77(i, &ct);
      PIAUTO::chassis::CanTransmitter::CanParse radarParse = std::bind(&PIAUTO::chassis::Radar_77::UpdateAttributes, radars[i], std::placeholders::_1);
      ct.registerCallbacks(radarParse);
  }

  // radar data buffer
  std::vector<PIAUTO::chassis::ObjectInfo_77> radarObjs[RADAR77_NUM][DEFAULT_BUFFER_SIZE];

  // x: -6 - 6
  // y: -6 - 6
  cv::Size map_size(1200, 1200);
  double size_per_pixel = 0.01;
  OccupancyStatusGridMap *OGM = new OccupancyStatusGridMap(size_per_pixel, map_size);

  cv::Mat car;
  cv::Mat temp_car = cv::imread("../../res/biro.png", CV_LOAD_IMAGE_COLOR);
  if (temp_car.data != nullptr) {
    double scale = (1.7 / OGM->cell_size()) / (temp_car.size().height);
    cv::resize(temp_car, car, cv::Size(), scale, scale, cv::INTER_LINEAR);
  }

  PIAUTO::sensor::SensorCoordinate _sc;

  leftRadarFile.open("./left_radar_data.txt", ios::out);
  middleRadarFile.open("./middle_radar_data.txt", ios::out);
  rightRadarFile.open("./right_radar_data.txt", ios::out);
  overallRadarFile.open("./overall_radar_data.txt", ios::out);

  while (1) {
    #if DEBUG
    std::thread::id main_id = std::this_thread::get_id();
    cout << "[" << __func__ << "] in thread(" << main_id << ")" << endl;
    #endif

    OGM->Reset();

    // x: vertical, up+, down-; y: horizontal, left+, right-
    OGM->DrawLineInMap(cv::Point2d(-1, -6), cv::Point2d(-1, 6), CellStatus::UNKNOWN);
    OGM->DrawLineInMap(cv::Point2d(-2, -6), cv::Point2d(-2, 6), CellStatus::UNKNOWN);
    OGM->DrawLineInMap(cv::Point2d(0, 6), cv::Point2d(0, -6), CellStatus::UNKNOWN);
    OGM->DrawLineInMap(cv::Point2d(-6, 0), cv::Point2d(6, 0), CellStatus::UNKNOWN);
    OGM->DrawLineInMap(cv::Point2d(1, -6), cv::Point2d(1, 6), CellStatus::UNKNOWN);
    OGM->DrawLineInMap(cv::Point2d(2, -6), cv::Point2d(2, 6), CellStatus::UNKNOWN);
    OGM->DrawLineInMap(cv::Point2d(3, -6), cv::Point2d(3, 6), CellStatus::UNKNOWN);
    OGM->DrawLineInMap(cv::Point2d(4, -6), cv::Point2d(4, 6), CellStatus::UNKNOWN);
    OGM->DrawLineInMap(cv::Point2d(5, -6), cv::Point2d(5, 6), CellStatus::UNKNOWN);
    OGM->DrawLineInMap(cv::Point2d(0, 0), cv::Point2d(6, 6), CellStatus::UNKNOWN);
    OGM->DrawLineInMap(cv::Point2d(0, 0), cv::Point2d(6, -6), CellStatus::UNKNOWN);
    OGM->DrawLineInMap(cv::Point2d(0, 0), cv::Point2d(6, 6 * tan(30 * M_PI / 180)), CellStatus::UNKNOWN);
    OGM->DrawLineInMap(cv::Point2d(0, 0), cv::Point2d(6, -6 * tan(30 * M_PI / 180)), CellStatus::UNKNOWN);
    OGM->DrawLineInMap(cv::Point2d(0, 0), cv::Point2d(6 / tan(60 * M_PI / 180), 6), CellStatus::UNKNOWN);
    OGM->DrawLineInMap(cv::Point2d(0, 0), cv::Point2d(6 / tan(60 * M_PI / 180), -6), CellStatus::UNKNOWN);
    OGM->DrawLineInMap(cv::Point2d(0, 0), cv::Point2d(-6 * tan(15 * M_PI / 180), 6), CellStatus::UNKNOWN);
    OGM->DrawLineInMap(cv::Point2d(0, 0), cv::Point2d(-6 * tan(15 * M_PI / 180), -6), CellStatus::UNKNOWN);

    // Adds two lanes.
    for (int i = -1; i <= 5; i += 2) {
      for (int j = -4; j <= 4; j += 1) {
        OGM->DrawRectInMap(Rect(i, j, 0.07, 0.8), CellStatus::UNKNOWN);
      }
    }

    OGM->DrawRectInMap(Rect(1, 0, 0.2, 0.07), CellStatus::UNKNOWN);
    OGM->DrawRectInMap(Rect(2, 0, 0.2, 0.07), CellStatus::UNKNOWN);
    OGM->DrawRectInMap(Rect(3, 0, 0.2, 0.07), CellStatus::UNKNOWN);
    OGM->DrawRectInMap(Rect(4, 0, 0.2, 0.07), CellStatus::UNKNOWN);
    OGM->DrawRectInMap(Rect(0, 0, 0.4, 0.14), CellStatus::UNKNOWN);
    OGM->DrawRectInMap(Rect(5, 0, 0.4, 0.14), CellStatus::UNKNOWN);
    OGM->DrawLineInMap(cv::Point2d(-0.2, 0.5 * VEHICLE_WIDTH + 0.2), cv::Point2d(0.2, 0.5 * VEHICLE_WIDTH - 0.2), CellStatus::UNKNOWN);
    OGM->DrawLineInMap(cv::Point2d(-0.2, -0.5 * VEHICLE_WIDTH - 0.2), cv::Point2d(0.2, -0.5 * VEHICLE_WIDTH + 0.2), CellStatus::UNKNOWN);
    OGM->DrawRectInMap(Rect(6, 0, 0.2, 0.07), CellStatus::UNKNOWN);
    OGM->DrawRectInMap(Rect(-1, 0, 0.2, 0.07), CellStatus::UNKNOWN);
    OGM->DrawRectInMap(Rect(-2, 0, 0.2, 0.07), CellStatus::UNKNOWN);

    for (int i = 0; i != RADAR77_NUM; ++i) {
      radars[i]->GetObjectInfoByTimes(radarObjs[i], DEFAULT_BUFFER_SIZE);
      for (int j = 0; j != DEFAULT_BUFFER_SIZE; ++j) {
        if (radarObjs[i][j].size() > 0 && radarObjs[i][j].size() <= 64) {
          #if DEBUG
          printf("radarObjs[%d][%d].size: %ld\n", i, j, radarObjs[i][j].size());
          #endif
          if (0 == i) {
            middleRadarFile << "middle, radarObs[0][" << j << "].size: " << radarObjs[0][j].size() << std::endl;
          } else if (1 == i) {
            leftRadarFile << "left, radarObs[1][" << j << "].size: " << radarObjs[1][j].size() << std::endl;
          } else if (2 == i) {
            rightRadarFile << "right, radarObs[2][" << j << "].size: " << radarObjs[2][j].size() << std::endl;
          }

          for (auto &object_info : radarObjs[i][j]) {
            logToFile(i, object_info);

            Eigen::Vector3d coordinate = _sc.Radar77Obj2Coordinate(object_info, i);
            if (0 == i) {
              overallRadarFile << "Sensor coordinate: [middle] " << object_info << ", world coordinate: (" << coordinate.x() << ", " << coordinate.y() << ")" << std::endl;
            } else if (1 == i) {
              overallRadarFile << "Sensor coordinate: [left] " << object_info << ", world coordinate: (" << coordinate.x() << ", " << coordinate.y() << ")" << std::endl;
            } else if (2 == i) {
              overallRadarFile << "Sensor coordinate: [right] " << object_info << ", world coordinate: (" << coordinate.x() << ", " << coordinate.y() << ")" << std::endl;
            }
            OGM->DrawRectInMap(Rect(coordinate.x(), coordinate.y(), 0.25, 0.07));
          }
        }
        radarObjs[i][j].clear();
      } // end of "for (int j = 0; j != DEFAULT_BUFFER_SIZE; ++j)"
    } // end of "for (int i = 0; i != RADAR77_NUM; ++i)"

    cv::Mat m = OGM->Visualize();
    // cv::namedWindow("map", cv::WINDOW_NORMAL);
    cv::namedWindow("map", cv::WINDOW_AUTOSIZE);
    cv::QtFont font = cv::fontQt("Times");
    cv::addText(m, "-2", cv::Point(604,795), font);
    cv::addText(m, "-1", cv::Point(604,695), font);
    cv::addText(m, "0", cv::Point(604,598), font);
    cv::addText(m, "1", cv::Point(604,498), font);
    cv::addText(m, "2", cv::Point(604,398), font);
    cv::addText(m, "3", cv::Point(604,298), font);
    cv::addText(m, "4", cv::Point(604,198), font);
    cv::addText(m, "5", cv::Point(604,98), font);
    cv::addText(m, "-3", cv::Point(280,604), font);
    cv::addText(m, "-2", cv::Point(380,604), font);
    cv::addText(m, "-1", cv::Point(480,604), font);
    cv::addText(m, "1", cv::Point(705,604), font);
    cv::addText(m, "2", cv::Point(805,604), font);
    cv::addText(m, "3", cv::Point(905,604), font);
    cv::addText(m, "-30deg", cv::Point(300,142), font);
    cv::addText(m, "-45deg", cv::Point(80,98), font);
    cv::addText(m, "-105deg", cv::Point(80,730), font);
    cv::addText(m, "30deg", cv::Point(860,142), font);
    cv::addText(m, "45deg", cv::Point(1080,98), font);
    cv::addText(m, "105deg", cv::Point(1080,730), font);
    // cv::namedWindow("map", cv::WINDOW_NORMAL);
    /* if (car.data != nullptr) {
      cv::Rect roi_rect(OGM->grid_size().width / 2 - car.cols / 2, OGM->grid_size().height / 2 - car.rows / 2, car.cols, car.rows);
      car.copyTo(m(roi_rect));
    } else {
      OGM->DrawRectInMap(Rect(0, 0, 1, 1.6));
    } */
    cv::imshow("map", m);
    if ('q' == cv::waitKey(20)) {
        break;
    }

    std::this_thread::sleep_for(std::chrono::milliseconds(10));
  }
  leftRadarFile.close();
  middleRadarFile.close();
  rightRadarFile.close();
  overallRadarFile.close();

  return 0;
}

void logByIndex(int index, std::string range_desc, PIAUTO::chassis::ObjectInfo_77 &object_info) {
  if (0 == index) {
    middleRadarFile << range_desc << object_info << std::endl;
  } else if (1 == index) {
    leftRadarFile << range_desc << object_info << std::endl;
  } else if (2 == index) {
    rightRadarFile << range_desc << object_info << std::endl;
  }
}

void logToFile(int index, PIAUTO::chassis::ObjectInfo_77 &object_info) {
  #if 1
  if (object_info.Range < 1.0) {
    logByIndex(index, "< 1.0  --  ", object_info);
  }
  #endif

  #if 1
  if (object_info.Range >= 1.0 && object_info.Range < 2.0) {
    logByIndex(index, ">= 1.0 && < 2.0  --  ", object_info);
  }
  #endif

  #if 1
  if (object_info.Range >= 2.0 && object_info.Range < 3.0) {
    logByIndex(index, ">= 2.0 && < 3.0  --  ", object_info);
  }
  #endif

  #if 1
  if (object_info.Range >= 3.0 && object_info.Range < 4.0) {
    logByIndex(index, ">= 3.0 && < 4.0  --  ", object_info);
  }
  #endif

  #if 1
  if (object_info.Range >= 4.0 && object_info.Range < 5.0) {
    logByIndex(index, ">= 4.0 && < 5.0  --  ", object_info);
  }
  #endif

  #if 1
  if (object_info.Range >= 5.0 && object_info.Range < 6.0) {
    logByIndex(index, ">= 5.0 && < 6.0  --  ", object_info);
  }
  #endif

  #if 0
  if (object_info.Range >= 6.0 && object_info.Range < 7.0) {
    logByIndex(index, ">= 6.0 && < 7.0  --  ", object_info);
  }
  #endif
  #if 0
  if (object_info.Range >= 7.0 && object_info.Range < 8.0) {
    logByIndex(index, ">= 7.0 && < 8.0  --  ", object_info);
  }
  #endif
  #if 0
  if (object_info.Range >= 8.0 && object_info.Range < 9.0) {
    logByIndex(index, ">= 8.0 && < 9.0  --  ", object_info);
  }
  #endif
  #if 0
  if (object_info.Range >= 9.0 && object_info.Range < 10.0) {
    logByIndex(index, ">= 9.0 && < 10.0  --  ", object_info);
  }
  #endif
  #if 0
  if (object_info.Range >= 10.0 && object_info.Range < 11.0) {
    logByIndex(index, ">= 10.0 && < 11.0  --  ", object_info);
  }
  #endif
  #if 0
  if (object_info.Range >= 11.0 && object_info.Range < 12.0) {
    logByIndex(index, ">= 11.0 && < 12.0  --  ", object_info);
  }
  #endif
  #if 0
  if (object_info.Range >= 12.0 && object_info.Range < 13.0) {
    logByIndex(index, ">= 12.0 && < 13.0  --  ", object_info);
  }
  #endif
  #if 0
  if (object_info.Range >= 13.0 && object_info.Range < 14.0) {
    logByIndex(index, ">= 13.0 && < 14.0  --  ", object_info);
  }
  #endif
  #if 0
  if (object_info.Range >= 14.0 && object_info.Range < 15.0) {
    logByIndex(index, ">= 14.0 && < 15.0  --  ", object_info);
  }
  #endif
  #if 0
  if (object_info.Range >= 15.0 && object_info.Range < 16.0) {
    logByIndex(index, ">= 15.0 && < 16.0  --  ", object_info);
  }
  #endif
  #if 0
  if (object_info.Range >= 16.0 && object_info.Range < 17.0) {
    logByIndex(index, ">= 16.0 && < 17.0  --  ", object_info);
  }
  #endif
  #if 0
  if (object_info.Range >= 17.0 && object_info.Range < 18.0) {
    logByIndex(index, ">= 17.0 && < 18.0  --  ", object_info);
  }
  #endif
  #if 0
  if (object_info.Range >= 18.0 && object_info.Range < 19.0) {
    logByIndex(index, ">= 18.0 && < 19.0  --  ", object_info);
  }
  #endif
  #if 0
  if (object_info.Range >= 19.0 && object_info.Range < 20.0) {
    logByIndex(index, ">= 19.0 && < 20.0  --  ", object_info);
  }
  #endif
  #if 0
  if (object_info.Range >= 20.0 && object_info.Range < 21.0) {
    logByIndex(index, ">= 20.0 && < 21.0  --  ", object_info);
  }
  #endif
  #if 0
  if (object_info.Range >= 21.0 && object_info.Range < 22.0) {
    logByIndex(index, ">= 21.0 && < 22.0  --  ", object_info);
  }
  #endif
}
