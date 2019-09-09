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
                dist_x_name, dist_x_var = line.partition("distance_x: ")[::2]
                dist_x_item = dist_x_var.split(" ")[0]
                dist_x_val = float(dist_x_item)
                dist_y_name, dist_y_var = line.partition("distance_y: ")[::2]
                dist_y_item = dist_y_var.split(" ")[0]
                dist_y_val = float(dist_y_item)
                if (dist_x_val >= 4.0 and dist_x_val <= 7.0) and (dist_y_val >= -1.0 and dist_y_val <= 1.0):
                    np.savetxt(filter_file, np.array(line).reshape(1), fmt="%s")

if __name__ == "__main__":
    if len(sys.argv) == 2 or len(sys.argv) == 3:
        loadradar(sys.argv[1])
    else:
        print("Usage: " + sys.argv[0] + " radar.txt")
