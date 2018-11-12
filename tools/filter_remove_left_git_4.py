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
  with open(filename) as myfile:
    with open('filter.txt', 'w+') as filter_file:
            for line in myfile.readlines():
                line = line[:-1]    # deletes extra line
                if re.search("radarObjs", line, re.IGNORECASE):
                    np.savetxt(filter_file, np.array(line).reshape(1), fmt="%s")
                elif re.search("Angle", line, re.IGNORECASE):
                    name, var = line.partition("Angle: ")[::2]
                    angle_item = var.split(" ")[0]
                    angle = float(angle_item)
                    name, var = line.partition("distance: ")[::2]
                    distance_item = var.split(" ")[0]
                    distance = float(distance_item)
                    if (angle >= 0.0):
                        np.savetxt(filter_file, np.array(line).reshape(1), fmt="%s")

if __name__ == "__main__":
    if len(sys.argv) == 2:
        loadradar(sys.argv[1])
    else:
        print("Usage: " + sys.argv[0] + " radar.txt")
