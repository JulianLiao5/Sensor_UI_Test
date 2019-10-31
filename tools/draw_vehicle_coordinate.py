#!/usr/bin/env python
# coding=utf-8

from enum import Enum, unique


import math
import matplotlib.pyplot as plt
import numpy as np
import re
import sys


DEG2RAD = math.pi / 180

# 1. 连续丢1帧出现了多少次
# 2. 连续丢2帧出现了多少次
# 10. 连续丢10帧出现了多少次
                   ## distance_name, distance_var = line.partition("distance: ")[::2]
                   ## distance_item = distance_var.split(" ")[0]
                   ## distance = float(distance_item)
                   ## angle_name, angle_var = line.partition("Angle: ")[::2]
                   ## angle_item = angle_var.split(" ")[0]
                   ## angle = float(angle_item)

def loadradar(filename):
    vehicle_x = []
    vehicle_y = []
    with open(filename) as myfile:
            for line in myfile.readlines():
                line = line[:-1]    # deletes extra line
                item = line.split(",")
                vehicle_x.append(float(item[2]))
                vehicle_y.append(float(item[3]))

    return vehicle_x, vehicle_y

if __name__ == "__main__":
    if len(sys.argv) == 2:
        vehicle_x, vehicle_y = loadradar(sys.argv[1])
        fig = plt.figure("vehicle_x")
        plt.plot(vehicle_x)
        plt.ylabel('vehicle_x')
        # plt.yticks(np.arange(int(np.min(distance)), int(np.max(distance)) + 1, 1))
        font = {'family': 'serif',
        'color':  'darkorchid',
        'weight': 'normal',
        'size': 14,
        }
        if False:
            plt.text(10, 15, "min: " + str(np.min(dist_x)) + ", mean: " +
                 "{0:.4f}".format(np.mean(dist_x)) + ", max: " + str(np.max(dist_x)), fontdict=font)
        else:
            plt.text(50, 8.05, "Ground truth: suppose 6.37m\n    min: " + str(np.min(vehicle_x)) + ", mean: " +
                 "{0:.4f}".format(np.mean(vehicle_x)) + ", max: " + str(np.max(vehicle_x)) + ", std dev: " + "{0:.4f}".format(np.std(vehicle_x)) +
                 "\n    error: " + "{:.4%}".format((np.mean(vehicle_x) - 6.37) / 6.37), fontdict=font)
        plt.grid(True)
        fig = plt.figure("vehicle_y")
        plt.plot(vehicle_y)
        plt.ylabel('vehicle_y')
        # plt.yticks(np.arange(int(np.min(distance)), int(np.max(distance)) + 1, 1))
        font = {'family': 'serif',
        'color':  'darkorchid',
        'weight': 'normal',
        'size': 14,
        }
        if False:
            plt.text(10, 15, "min: " + str(np.min(dist_x)) + ", mean: " +
                 "{0:.4f}".format(np.mean(dist_x)) + ", max: " + str(np.max(dist_x)), fontdict=font)
        else:
            plt.text(80, 0.3, "Ground truth: suppose -4.25m\n    min: " + str(np.min(vehicle_y)) + ", mean: " +
                 "{0:.4f}".format(np.mean(vehicle_y)) + ", max: " + str(np.max(vehicle_y)) + ", std dev: " + "{0:.4f}".format(np.std(vehicle_y)) +
                 "\n    error: " + "{:.4%}".format((np.mean(vehicle_y) + 4.25) / (-4.25)), fontdict=font)
        plt.grid(True)
        plt.show()
    else:
        print("Usage: " + sys.argv[0] + " radar.txt")
