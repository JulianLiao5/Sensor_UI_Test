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
    with open('filter_disty.txt', 'w+') as filter_file:
            for line in myfile.readlines():
                line = line[:-1]    # deletes extra line
                dist_name, dist_var = line.partition("distance: ")[::2]
                dist_item = dist_var.split(" ")[0]
                dist_val = float(dist_item)
                angle_name, angle_var = line.partition("Angle: ")[::2]
                angle_item = angle_var.split(" ")[0]
                angle_val = float(angle_item)
                if (dist_val >= 0.5 and dist_val <= 4.0) and (angle_val >= -70.0 and angle_val <= -30.0):
                    np.savetxt(filter_file, np.array(line).reshape(1), fmt="%s")

if __name__ == "__main__":
    if len(sys.argv) == 2 or len(sys.argv) == 3:
        loadradar(sys.argv[1])
    else:
        print("Usage: " + sys.argv[0] + " radar.txt")
