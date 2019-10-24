#!/usr/bin/env python
# coding=utf-8

import matplotlib.pyplot as plt
import numpy as np
import re
import sys

def loadradar(filename):
  distance = []
  velocity = []
  angle = []
  power = []
  last_line_vehicle = False
  with open(filename) as myfile:
    with open('filter_b.txt', 'w+') as filter_file:
            for line in myfile.readlines():
                line = line[:-1]    # deletes extra line
                if last_line_vehicle == True:
                    np.savetxt(filter_file, np.array(line).reshape(1), fmt="%s")
                if re.search("radar_coordinate", line, re.IGNORECASE):
                    last_line_vehicle = False
                    last_radar_line = line
                elif re.search("Angle", line, re.IGNORECASE) and re.search("distance", line, re.IGNORECASE):
                    last_line_vehicle = False
                    name, var = line.partition("Angle: ")[::2]
                    angle_item = var.split(" ")[0]
                    angle = float(angle_item)
                    name, var = line.partition("distance: ")[::2]
                    distance_item = var.split(" ")[0]
                    distance = float(distance_item)
                    #if ((distance >= 0.0 and distance < 50.0) and (angle >= -15.0 and angle <= 15.0)):
                    if ((distance >= 0.0 and distance < 5.0)):
                        qualified = True
                        np.savetxt(filter_file, np.array(last_radar_line).reshape(1), fmt="%s")
                        np.savetxt(filter_file, np.array(line).reshape(1), fmt="%s")
                    else:
                        qualified = False
                elif re.search("vehicle_coordinate", line):
                    if qualified == True:
                        last_line_vehicle = True
                        np.savetxt(filter_file, np.array(line).reshape(1), fmt="%s")
                    else:
                        last_line_vehicle = False
                else:
                    last_line_vehicle = False

if __name__ == "__main__":
    if len(sys.argv) == 2:
        loadradar(sys.argv[1])
    else:
        print("Usage: " + sys.argv[0] + " radar.txt")
