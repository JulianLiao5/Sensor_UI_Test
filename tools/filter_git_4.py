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
    with open('filter.txt', 'w+') as filter_file:
            for line in myfile.readlines():
                line = line[:-1]    # deletes extra line
                if re.search("radarObjs", line, re.IGNORECASE):
                    np.savetxt(filter_file, np.array(line).reshape(1), fmt="%s")
                elif re.search("Angle", line, re.IGNORECASE):
                    index_name, index_var = line.partition("index: ")[::2]
                    index_item = index_var.split(" ")[0]
                    if len(sys.argv) == 3 and int(index_item) != int(sys.argv[2]):
                      np.savetxt(filter_file, np.array(line).reshape(1), fmt="%s")

if __name__ == "__main__":
    if len(sys.argv) == 2 or len(sys.argv) == 3:
        loadradar(sys.argv[1])
    else:
        print("Usage: " + sys.argv[0] + " radar.txt")
