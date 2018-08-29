//
// Created by mikaa-mi on 18-4-19.
//

#include <utils/sensor_coordinate.h>

namespace PIAUTO {
    namespace sensor {

        SensorCoordinate::SensorCoordinate() {
            world_to_map_radar[0] << 1.0, 0.0, 0.8,
                    0.0, 1.0, 0.0,
                    0.0, 0.0, 1.0;

            double num_temp=std::sqrt(2)/2;
            world_to_map_radar[1] << num_temp, -num_temp, 0.4,
                    num_temp, num_temp, 0.6,
                    0.0, 0.0, 1.0;

            world_to_map_radar[2] << num_temp, num_temp, 0.4,
                    -num_temp, num_temp, -0.6,
                    0.0, 0.0, 1.0;
        }

        Eigen::Vector3d SensorCoordinate::Radar77Obj2Coordinate(const chassis::ObjectInfo_77 &obj, int index){
            Eigen::Vector3d coordinate(0.0, 0.0, 1.0);
            coordinate.x() = obj.Range * cosf(obj.Azimuth * M_PI / 180);
            coordinate.y() = -obj.Range * sinf(obj.Azimuth * M_PI / 180);
            coordinate = world_to_map_radar[index] * coordinate;

            return coordinate;
        };

    }
}
