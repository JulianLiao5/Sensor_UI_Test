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
                dist_y_name, dist_y_var = line.partition("distance_y: ")[::2]
                dist_y_item = dist_y_var.split(" ")[0]
                dist_y_val = float(dist_y_item)
                if (dist_y_val >= -0.458441 and dist_y_val < 0.0) or (dist_y_val >= 0.0 and dist_y_val <= 0.458441):
                    np.savetxt(filter_file, np.array(line).reshape(1), fmt="%s")

if __name__ == "__main__":
    if len(sys.argv) == 2 or len(sys.argv) == 3:
        loadradar(sys.argv[1])
    else:
        print("Usage: " + sys.argv[0] + " radar.txt")
