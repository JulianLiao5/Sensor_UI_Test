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
                if re.search("radarObjs", line, re.IGNORECASE):
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
                    name, var = line.partition("distance_x: ")[::2]
                    distance_x_item = var.split(" ")[0]
                    distance_x.append(float(distance_x_item))
                    name, var = line.partition("distance_y: ")[::2]
                    distance_y_item = var.split(" ")[0]
                    distance_y.append(float(distance_y_item))
                    name, var = line.partition("RadialVelocity: ")[::2]
                    velocity_item = var.split(" ")[0]
                    velocity.append(float(velocity_item))
                    name, var = line.partition("Power: ")[::2]
                    power_item = var.split(" ")[0]
                    power.append(float(power_item))
  print("ONE_size: " + str(len(ONE)) + ", TWO size: " + str(len(TWO)) + ", THREE size: " + str(len(THREE)) + ", FOUR size: " + str(len(FOUR)) + ", FIVE_size: " + str(len(FIVE)) + ", SIX_size: " + str(len(SIX)))
  print("frame_cnt: " + str(frame_cnt))
  return index, distance_x, distance_y, distance, velocity, angle, power, detect_num

if __name__ == "__main__":
    if len(sys.argv) == 3 or len(sys.argv) == 2:
        index, distance_x, distance_y, distance, velocity, angle, power, detect_num = loadradar(sys.argv[1])
        indexset = set(index)
        print("    indexset: " + str(indexset) + "\n    indexset length: " + str(len(indexset)))
        distance_x_2 = []
        distance_y_2 = []
        distance_2 = []
        angle_2 = []
        power_2 = []
        distance_certain = []
        angle_certain = []
        power_certain = []
        for index_item in indexset:
            with open(sys.argv[1]) as myfile:
                del distance_x_2[:]
                del distance_y_2[:]
                del distance_2[:]
                del angle_2[:]
                del power_2[:]
                for line in myfile.readlines():
                    line = line[:-1]    # deletes extra line
                    if re.search(r"\index: " + str(index_item) + " ", line, re.IGNORECASE):
                        name, var = line.partition("distance_x: ")[::2]
                        distance_x_item = var.split(" ")[0]
                        distance_x_2.append(float(distance_x_item))
                        name, var = line.partition("distance_y: ")[::2]
                        distance_y_item = var.split(" ")[0]
                        distance_y_2.append(float(distance_y_item))
                        name, var = line.partition("distance: ")[::2]
                        distance_item = var.split(" ")[0]
                        distance_2.append(float(distance_item))
                        if len(sys.argv) == 3 and index_item == int(sys.argv[2]):
                            distance_certain.append(float(distance_item))
                        name, var = line.partition("Angle: ")[::2]
                        angle_item = var.split(" ")[0]
                        angle_2.append(float(angle_item))
                        if len(sys.argv) == 3 and index_item == int(sys.argv[2]):
                            angle_certain.append(float(angle_item))
                        name, var = line.partition("Power: ")[::2]
                        power_item = var.split(" ")[0]
                        power_2.append(float(power_item))
                        if len(sys.argv) == 3 and index_item == int(sys.argv[2]):
                            power_certain.append(float(power_item))
                print("        num(index_" + str(index_item) + "): len: "+ str(len(angle_2))  + ", distance_x: [" +
                                    str(np.min(distance_x_2)) + "  --  " + str(np.max(distance_x_2))+ "], distance_y: [" +
                                    str(np.min(distance_y_2)) + "  --  " + str(np.max(distance_y_2))+ "], distance: [" +
                                    str(np.min(distance_2)) + "  --  " + str(np.max(distance_2)) + "], angle: [" +
                                    str(np.min(angle_2)) + "  --  " + str(np.max(angle_2)) + "]" + "], power: [" +
                                    str(np.min(power_2)) + "  --  " + str(np.max(power_2)) + "]")
        dist_x_max = np.max(distance_x)
        dist_x_min = np.min(distance_x)
        dist_y_max = np.max(distance_y)
        dist_y_min = np.min(distance_y)
        dist_max = np.max(distance)
        dist_min = np.min(distance)
        velocity_max = np.max(velocity)
        velocity_min = np.min(velocity)
        angle_max = np.max(angle)
        angle_min = np.min(angle)
        power_max = np.max(power)
        power_min = np.min(power)
        print("distance_x: [" + str(dist_x_min) + "  --  " + str(dist_x_max)  + "]\ndistance_y: [" + str(dist_y_min) + "  --  " + str(dist_y_max)  + "]\ndistance: [" + str(dist_min) + "  --  " + str(dist_max)  + "]\nvelocity: [" + str(velocity_min) + "  --  " + str(velocity_max) + "]\nangle: [" + str(angle_min) + "  --  " + str(angle_max) + "]\npower: [" + str(power_min) + "  --  " + str(power_max) + "]\n")
        if True:
            fig = plt.figure("detect_num")
            plt.plot(detect_num)
            plt.grid(True)
            font = {'family': 'serif',
            'color':  'darkred',
            'weight': 'normal',
            'size': 14,
            }
            plt.show()
        if len(sys.argv) == 3: 
            fig = plt.figure("certain_distance")
            plt.plot(distance_certain)
            plt.title("Index: " + sys.argv[2])
            plt.grid(True)
            fig = plt.figure("certain_angle")
            plt.plot(angle_certain)
            plt.title("Index: " + sys.argv[2])
            plt.grid(True)
            fig = plt.figure("certain_power")
            plt.plot(power_certain)
            plt.title("Index: " + sys.argv[2])
            plt.grid(True)
            plt.show()
    else:
        print("Usage: " + sys.argv[0] + " radar.txt")
