#!/usr/bin/env python
# coding=utf-8

import inspect
import matplotlib.pyplot as plt
import numpy as np
import re
import sys

def lineno():
    """Returns the current line number in our program."""
    return inspect.currentframe().f_back.f_lineno

def loadradar(filename):
  index = []
  distance_x = []
  distance_y = []
  distance = []
  velocity = []
  angle = []
  power = []
  detect_num = []
  ONE = []
  TWO = []
  THREE = []
  FOUR = []
  FIVE = []
  SIX = []
  CNT = 0
  frame_cnt = 0
  with open(filename) as myfile:
            for line in myfile.readlines():
                line = line[:-1]    # deletes extra line
                if re.search("buff", line, re.IGNORECASE):
                    frame_cnt += 1
                    if CNT == 1:
                        detect_num.append(1)
                        ONE.append(1)
                    elif CNT == 2:
                        detect_num.append(2)
                        TWO.append(2)
                    elif CNT == 3:
                        detect_num.append(3)
                        THREE.append(3)
                    elif CNT == 4:
                        detect_num.append(4)
                        FOUR.append(4)
                    elif CNT == 5:
                        detect_num.append(5)
                        FIVE.append(5)
                    elif CNT == 6:
                        detect_num.append(6)
                        SIX.append(6)
                    CNT = 0
                elif re.search("Angle", line, re.IGNORECASE):
                    CNT += 1
                    name, var = line.partition("index: ")[::2]
                    index_item = var.split(" ")[0]
                    index.append(int(index_item))
                    name, var = line.partition("Angle: ")[::2]
                    angle_item = var.split(" ")[0]
                    angle.append(float(angle_item))
                    name, var = line.partition("distance: ")[::2]
                    distance_item = var.split(" ")[0]
                    distance.append(float(distance_item))
                    name, var = line.partition("RadialVelocity: ")[::2]
                    velocity_item = var.split(" ")[0]
                    velocity.append(float(velocity_item))
                    name, var = line.partition("Power: ")[::2]
                    power_item = var.split(" ")[0]
                    power.append(float(power_item))
  print("frame_cnt: " + str(frame_cnt))
  return index, distance, velocity, angle, power, detect_num

if __name__ == "__main__":
    if len(sys.argv) == 3 or len(sys.argv) == 2:
        index, distance, velocity, angle, power, detect_num = loadradar(sys.argv[1])


        power_max = np.max(power)
        power_min = np.min(power)
        fig = plt.figure("power")
        plt.plot(power)
        plt.grid(True)
        font = {'family': 'serif',
        'color':  'darkred',
        'weight': 'normal',
        'size': 16,
        }
        plt.text(2000, -55, "CNT: " + str(len(power)) + " | power_min:    " + str(power_min) + ", max : "  + str(power_max) + "\n", fontdict=font)
        plt.title("Power statistics")
        plt.show()

    else:
        print("Usage: " + sys.argv[0] + " radar.txt")
