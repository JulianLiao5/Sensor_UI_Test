/*************************************************************************
	> File Name: test_ogm.cpp
	> Author: 
	> Mail: 
	> Created Time: 2018年08月28日 星期二 14时41分45秒
 ************************************************************************/

#include<iostream>

#include <opencv2/core.hpp>

#include <utils/sensor_coordinate.h>
#include <utils/occupancy_status_grid_map.h>

using namespace std;

#define TIME_0    0x00
#define TIME_1    0x1C

int main(int argc, char *argv[]) {
  PIAUTO::sensor::SensorCoordinate _sc;

  PIAUTO::chassis::Radar_77 *radars[RADAR77_NUM];
  PIAUTO::chassis::CanTransmitter ct(VCI_USBCAN2, 0, 0, 0, 0, 0, 0, TIME_0, TIME_1);
  for (int i = 0; i < RADAR77_NUM; i++) {
    radars[i] = new PIAUTO::chassis::Radar_77(i, &ct);
  }

  // radar data buffer
  std::vector<PIAUTO::chassis::ObjectInfo_77> radarObjs[RADAR77_NUM][20];

  cv::Size map_size(800, 800);
  double size_per_pixel = 0.05;
  OccupancyStatusGridMap *OGM = new OccupancyStatusGridMap(size_per_pixel, map_size);

  cv::Mat car;
  cv::Mat temp_car = cv::imread("../../res/biro.png", CV_LOAD_IMAGE_COLOR);
  if (temp_car.data != nullptr) {
    double scale = (1.7 / OGM->cell_size()) / (temp_car.size().height);
    cv::resize(temp_car, car, cv::Size(), scale, scale, cv::INTER_LINEAR);
  }

  if (car.data == nullptr) {
    OGM->DrawRectInMap(Rect(0, 0, 1, 1.6));
  }

  while (1) {
    OGM->Reset();

    OGM->DrawLineInMap(cv::Point2d(0, 20), cv::Point2d(0, -20), CellStatus::UNKNOWN);
    OGM->DrawLineInMap(cv::Point2d(-20, 0), cv::Point2d(20, 0), CellStatus::UNKNOWN);
    OGM->DrawLineInMap(cv::Point2d(0, 0), cv::Point2d(20, 20), CellStatus::UNKNOWN);
    OGM->DrawLineInMap(cv::Point2d(0, 0), cv::Point2d(20, -20), CellStatus::UNKNOWN);

    for (int i = -2; i <= 16; i += 3) {
      for (int j = -6; j <= 6; j += 4) {
        OGM->DrawRectInMap(Rect(i, j, 0.11, 2), CellStatus::UNKNOWN);
      }
    }

    OGM->DrawRectInMap(Rect(0, 0, 0.2, 0.11), CellStatus::UNKNOWN);
    OGM->DrawRectInMap(Rect(5, 0, 0.2, 0.11), CellStatus::UNKNOWN);
    OGM->DrawRectInMap(Rect(10, 0, 0.2, 0.11), CellStatus::UNKNOWN);
    OGM->DrawRectInMap(Rect(15, 0, 0.2, 0.11), CellStatus::UNKNOWN);

    for (int i = 0; i != RADAR77_NUM; ++i) {
      radars[i]->GetObjectInfoByTimes(radarObjs[i], 20);
      for (int j = 0; j != 20; ++j) {
        for (auto &object_temp : radarObjs[i][j]) {
          Eigen::Vector3d coordinate = _sc.Radar77Obj2Coordinate(object_temp, i);
          OGM->DrawRectInMap(Rect(coordinate.x(), coordinate.y(), 0.5, 0.11));
        }
      }
    }

    cv::Mat m = OGM->Visualize();
    // cv::namedWindow("map", cv::WINDOW_NORMAL);
    if (car.data != nullptr) {
      cv::Rect roi_rect(OGM->grid_size().width / 2 - car.cols / 2, OGM->grid_size().height / 2 - car.rows / 2, car.cols, car.rows);
      car.copyTo(m(roi_rect));
    }
    cv::imshow("map", m);
    if ('q' == cv::waitKey(20)) {
        break;
    }
  }

  return 0;
}
