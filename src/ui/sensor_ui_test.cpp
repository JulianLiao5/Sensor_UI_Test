/*************************************************************************
	> File Name: test_ogm.cpp
	> Author: 
	> Mail: 
	> Created Time: 2018年08月28日 星期二 14时41分45秒
 ************************************************************************/

#include<functional>
#include <math.h>
#include<iostream>

#include <opencv2/core.hpp>

#include <utils/sensor_coordinate.h>
#include <utils/occupancy_status_grid_map.h>

using namespace std;

#define TIME_0    0x00
#define TIME_1    0x1C

int main(int argc, char *argv[]) {
  PIAUTO::chassis::Radar_77 *radars[RADAR77_NUM];
  PIAUTO::chassis::CanTransmitter ct(VCI_USBCAN2, 0, 0, 0, 0, 0, 0, TIME_0, TIME_1);
  for (int i = 0; i < RADAR77_NUM; i++) {
      radars[i] = new PIAUTO::chassis::Radar_77(i, &ct);
      PIAUTO::chassis::CanTransmitter::CanParse radarParse = std::bind(&PIAUTO::chassis::Radar_77::UpdateAttributes, radars[i], std::placeholders::_1);
      ct.registerCallbacks(radarParse);
  }

  // radar data buffer
  std::vector<PIAUTO::chassis::ObjectInfo_77> radarObjs[RADAR77_NUM][DEFAULT_BUFFER_SIZE];

  cv::Size map_size(1000, 1000);
  double size_per_pixel = 0.05;
  OccupancyStatusGridMap *OGM = new OccupancyStatusGridMap(size_per_pixel, map_size);

  cv::Mat car;
  cv::Mat temp_car = cv::imread("../../res/biro.png", CV_LOAD_IMAGE_COLOR);
  if (temp_car.data != nullptr) {
    double scale = (1.7 / OGM->cell_size()) / (temp_car.size().height);
    cv::resize(temp_car, car, cv::Size(), scale, scale, cv::INTER_LINEAR);
  }

  PIAUTO::sensor::SensorCoordinate _sc;

  while (1) {
    #if DEBUG
    std::thread::id main_id = std::this_thread::get_id();
    cout << "[" << __func__ << "] in thread(" << main_id << ")" << endl;
    #endif

    OGM->Reset();

    OGM->DrawLineInMap(cv::Point2d(0, 25), cv::Point2d(0, -25), CellStatus::UNKNOWN);
    OGM->DrawLineInMap(cv::Point2d(-25, 0), cv::Point2d(25, 0), CellStatus::UNKNOWN);
    OGM->DrawLineInMap(cv::Point2d(0, 0), cv::Point2d(25, 25), CellStatus::UNKNOWN);
    OGM->DrawLineInMap(cv::Point2d(0, 0), cv::Point2d(25, -25), CellStatus::UNKNOWN);
    OGM->DrawLineInMap(cv::Point2d(0, 0), cv::Point2d(25, 25 * tan(30 * M_PI / 180)), CellStatus::UNKNOWN);
    OGM->DrawLineInMap(cv::Point2d(0, 0), cv::Point2d(25, -25 * tan(30 * M_PI / 180)), CellStatus::UNKNOWN);
    OGM->DrawLineInMap(cv::Point2d(0, 0), cv::Point2d(25 / tan(60 * M_PI / 180), 25), CellStatus::UNKNOWN);
    OGM->DrawLineInMap(cv::Point2d(0, 0), cv::Point2d(25 / tan(60 * M_PI / 180), -25), CellStatus::UNKNOWN);

    for (int i = -2; i <= 16; i += 3) {
      for (int j = -6; j <= 6; j += 4) {
        OGM->DrawRectInMap(Rect(i, j, 0.11, 2), CellStatus::UNKNOWN);
      }
    }

    OGM->DrawRectInMap(Rect(1, 0, 0.2, 0.11), CellStatus::UNKNOWN);
    OGM->DrawRectInMap(Rect(2, 0, 0.2, 0.11), CellStatus::UNKNOWN);
    OGM->DrawRectInMap(Rect(3, 0, 0.2, 0.11), CellStatus::UNKNOWN);
    OGM->DrawRectInMap(Rect(4, 0, 0.2, 0.11), CellStatus::UNKNOWN);
    OGM->DrawRectInMap(Rect(0, 0, 0.4, 0.22), CellStatus::UNKNOWN);
    OGM->DrawRectInMap(Rect(5, 0, 0.4, 0.22), CellStatus::UNKNOWN);
    OGM->DrawRectInMap(Rect(10, 0, 0.4, 0.22), CellStatus::UNKNOWN);
    OGM->DrawRectInMap(Rect(15, 0, 0.4, 0.22), CellStatus::UNKNOWN);
    OGM->DrawRectInMap(Rect(20, 0, 0.4, 0.22), CellStatus::UNKNOWN);
    OGM->DrawRectInMap(Rect(16, 0, 0.2, 0.11), CellStatus::UNKNOWN);
    OGM->DrawRectInMap(Rect(17, 0, 0.2, 0.11), CellStatus::UNKNOWN);
    OGM->DrawRectInMap(Rect(18, 0, 0.2, 0.11), CellStatus::UNKNOWN);
    OGM->DrawRectInMap(Rect(19, 0, 0.2, 0.11), CellStatus::UNKNOWN);

    for (int i = 0; i != RADAR77_NUM; ++i) {
      radars[i]->GetObjectInfoByTimes(radarObjs[i], DEFAULT_BUFFER_SIZE);
      for (int j = 0; j != DEFAULT_BUFFER_SIZE; ++j) {
        if (radarObjs[i][j].size() > 0 && radarObjs[i][j].size() <= 64) {
          #if DEBUG
          printf("radarObjs[%d][%d].size: %ld\n", i, j, radarObjs[i][j].size());
          #endif
          for (auto &object_temp : radarObjs[i][j]) {
              #if 0
              if (object_temp.Range < 1.0) {
                      std::cout << "< 1.0  --  " << object_temp << std::endl;
              }
              #endif
              #if 0
              if (object_temp.Range >= 1.0 && object_temp.Range < 2.0) {
                      std::cout << ">= 1.0 && < 2.0  --  " << object_temp << std::endl;
              }
              #endif
              #if 0
              if (object_temp.Range >= 2.0 && object_temp.Range < 3.0) {
                      std::cout << ">= 2.0 && < 3.0  --  " << object_temp << std::endl;
              }
              #endif
              #if 0
              if (object_temp.Range >= 3.0 && object_temp.Range < 4.0) {
                      std::cout << ">= 3.0 && < 4.0  --  " << object_temp << std::endl;
              }
              #endif
              #if 0
              if (object_temp.Range >= 4.0 && object_temp.Range < 5.0) {
                      std::cout << ">= 4.0 && < 5.0  --  " << object_temp << std::endl;
              }
              #endif
              #if 0
              if (object_temp.Range >= 5.0 && object_temp.Range < 6.0) {
                      std::cout << ">= 5.0 && < 6.0  --  " << object_temp << std::endl;
              }
              #endif
              #if 0
              if (object_temp.Range >= 6.0 && object_temp.Range < 7.0) {
                      std::cout << ">= 6.0 && < 7.0  --  " << object_temp << std::endl;
              }
              #endif
              #if 0
              if (object_temp.Range >= 7.0 && object_temp.Range < 8.0) {
                      std::cout << ">= 7.0 && < 8.0  --  " << object_temp << std::endl;
              }
              #endif
              #if 0
              if (object_temp.Range >= 8.0 && object_temp.Range < 9.0) {
                      std::cout << ">= 8.0 && < 9.0  --  " << object_temp << std::endl;
              }
              #endif
              #if 0
              if (object_temp.Range >= 9.0 && object_temp.Range < 10.0) {
                      std::cout << ">= 9.0 && < 10.0  --  " << object_temp << std::endl;
              }
              #endif
              #if 0
              if (object_temp.Range >= 10.0 && object_temp.Range < 11.0) {
                      std::cout << ">= 10.0 && < 11.0  --  " << object_temp << std::endl;
              }
              #endif
              #if 0
              if (object_temp.Range >= 11.0 && object_temp.Range < 12.0) {
                      std::cout << ">= 11.0 && < 12.0  --  " << object_temp << std::endl;
              }
              #endif
              #if 0
              if (object_temp.Range >= 12.0 && object_temp.Range < 13.0) {
                      std::cout << ">= 12.0 && < 13.0  --  " << object_temp << std::endl;
              }
              #endif
              #if 0
              if (object_temp.Range >= 13.0 && object_temp.Range < 14.0) {
                      std::cout << ">= 13.0 && < 14.0  --  " << object_temp << std::endl;
              }
              #endif
              #if 0
              if (object_temp.Range >= 14.0 && object_temp.Range < 15.0) {
                      std::cout << ">= 14.0 && < 15.0  --  " << object_temp << std::endl;
              }
              #endif
              #if 0
              if (object_temp.Range >= 15.0 && object_temp.Range < 16.0) {
                      std::cout << ">= 15.0 && < 16.0  --  " << object_temp << std::endl;
              }
              #endif


            Eigen::Vector3d coordinate = _sc.Radar77Obj2Coordinate(object_temp, i);
            OGM->DrawRectInMap(Rect(coordinate.x(), coordinate.y(), 0.5, 0.11));
          }
        }
        radarObjs[i][j].clear();
      }
    }

    cv::Mat m = OGM->Visualize();
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

  return 0;
}
