#!/usr/bin/env python
# coding=utf-8

import math
import matplotlib.pyplot as plt
import numpy as np
import re
import sys

DEG2RAD = math.pi / 180

def loadradar(filename):
  distance = []
  velocity = []
  angle = []
  power = []
  with open(filename) as myfile:
    with open('transfer.txt', 'w+') as filter_file:
            for line in myfile.readlines():
                line = line[:-1]    # deletes extra line
                if re.search("Angle", line, re.IGNORECASE):
                    angle_name, angle_var = line.partition("Angle: ")[::2]
                    angle_item = angle_var.split(" ")[0]
                    angle = float(angle_item)
                    distance_name, distance_var = line.partition("distance: ")[::2]
                    distance_item = distance_var.split(" ")[0]
                    distance = float(distance_item)
                    distance_x = distance * math.cos(angle * DEG2RAD)
                    distance_y = -(distance * math.sin(angle * DEG2RAD))
                    new_line = distance_name + "distance_x: " + "{0:.4f}".format(distance_x) + " distance_y: " + "{0:.4f}".format(distance_y) + " distance: " + distance_var
                    np.savetxt(filter_file, np.array(new_line).reshape(1), fmt="%s")

if __name__ == "__main__":
    if len(sys.argv) == 2:
        loadradar(sys.argv[1])
    else:
        print("Usage: " + sys.argv[0] + " radar.txt")
