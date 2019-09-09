#!/usr/bin/env python
# coding=utf-8

from enum import Enum, unique


import math
import matplotlib.pyplot as plt
import numpy as np
import re
import sys

class LineType(Enum):
    Line_Unknown = 0
    Line_radar_coordinate = 1

DEG2RAD = math.pi / 180

# 1. 连续丢1帧出现了多少次
# 2. 连续丢2帧出现了多少次
# 10. 连续丢10帧出现了多少次

def loadradar(filename):
  lineno = 0
  last_Line_Type = LineType.Line_Unknown
  cur_Line_Type = LineType.Line_Unknown
  with open(filename) as myfile:
    with open('filter_vehicle_coordinate.txt', 'w+') as filter_file:
            for line in myfile.readlines():
                line = line[:-1]    # deletes extra line

                if LineType.Line_radar_coordinate == last_Line_Type:
                    np.savetxt(filter_file, np.array(line).reshape(1), fmt="%s")

                if re.search("radar_coordinate", line, re.IGNORECASE):
                    distance_name, distance_var = line.partition("distance: ")[::2]
                    distance_item = distance_var.split(" ")[0]
                    distance = float(distance_item)
                    angle_name, angle_var = line.partition("Angle: ")[::2]
                    angle_item = angle_var.split(" ")[0]
                    angle = float(angle_item)
                    if (distance >= 4.0 and distance <= 6.0) and (angle >= -5.0 and angle <= 5.0):
                        cur_Line_Type = LineType.Line_radar_coordinate
                    else:
                        cur_Line_Type = LineType.Line_Unknown
                else:
                    cur_Line_Type = LineType.Line_Unknown

                last_Line_Type = cur_Line_Type

if __name__ == "__main__":
    if len(sys.argv) == 2:
        loadradar(sys.argv[1])
    else:
        print("Usage: " + sys.argv[0] + " radar.txt")
