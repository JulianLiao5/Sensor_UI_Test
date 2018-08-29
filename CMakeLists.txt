cmake_minimum_required(VERSION 3.5)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wall -g -O3 -std=c++1y")

find_package(OpenCV REQUIRED)
include_directories(${OpenCV_INCLUDE_DIRS})

find_package(Glog REQUIRED)
include_directories(${GLOG_INCLUDE_DIR})

find_package(GFlags REQUIRED)
include_directories(${GFLAGS_INCLUDE_DIR})

include_directories(include)

add_executable(sensor_ui_test src/ui/sensor_ui_test.cpp src/can/CanNode.cpp src/can/CanTransmitter.cpp src/sensor/Radar77.cpp
    src/utils/occupancy_status_grid_map.cc src/utils/sensor_coordinate.cpp src/utils/PITime.cpp)
target_link_libraries(sensor_ui_test ${OpenCV_LIBS} usbcan glog gflags pthread)
