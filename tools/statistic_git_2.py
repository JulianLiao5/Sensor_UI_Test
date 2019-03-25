#!/usr/bin/env python
# coding=utf-8

from enum import Enum, unique


import math
import matplotlib.pyplot as plt
import numpy as np
import re
import sys

class LineType(Enum):
    Line_Unknown = 0
    Line_radarObjs = 1
    Line_Angle = 2

DEG2RAD = math.pi / 180

# 1. 连续丢1帧出现了多少次
# 2. 连续丢2帧出现了多少次
# 10. 连续丢10帧出现了多少次

def loadradar(filename):
  distance = []
  velocity = []
  angle = []
  power = []
  loss_cnt = []
  multi_cnt = []
  lineno = 0
  last_Line_Type = LineType.Line_Unknown
  cur_Line_Type = LineType.Line_Unknown
  last_radarObjs_lineno = 0
  cur_radarObjs_lineno = 0
  last_Angle_lineno = 0
  cur_Angle_lineno = 0
  with open(filename) as myfile:
    with open('statistic.txt', 'w+') as filter_file:
            for line in myfile.readlines():
                line = line[:-1]    # deletes extra line
                if re.search("buff", line, re.IGNORECASE):
                    cur_Line_Type = LineType.Line_radarObjs
                    last_radarObjs_line = line
                    cur_radarObjs_lineno = lineno
                    if LineType.Line_Angle == last_Line_Type:
                        this_multi_cnt = cur_radarObjs_lineno - last_radarObjs_lineno - 2
                        if this_multi_cnt >= 0:
                            multi_cnt.append(this_multi_cnt)
                elif re.search("Angle", line, re.IGNORECASE):
                    cur_Line_Type = LineType.Line_Angle
                    cur_Angle_lineno = lineno
                    if LineType.Line_radarObjs == last_Line_Type:
                        this_loss_cnt = cur_Angle_lineno - last_Angle_lineno - 2
                        if this_loss_cnt > 0:
                            loss_cnt.append(this_loss_cnt)
                        np.savetxt(filter_file, np.array(last_radarObjs_line).reshape(1), fmt="%s")
                    angle_name, angle_var = line.partition("Angle: ")[::2]
                    angle_item = angle_var.split(" ")[0]
                    angle = float(angle_item)
                    distance_name, distance_var = line.partition("distance: ")[::2]
                    distance_item = distance_var.split(" ")[0]
                    distance = float(distance_item)
                    np.savetxt(filter_file, np.array(line).reshape(1), fmt="%s")
                last_radarObjs_lineno = cur_radarObjs_lineno
                last_Angle_lineno = cur_Angle_lineno
                last_Line_Type = cur_Line_Type
                lineno = lineno + 1

            total_multi_cnt = sum(multi_cnt)
            multi_cnt_set = set(multi_cnt)
            print("Total multi cnt: " + str(total_multi_cnt) + ", total multi times: " + str(len(multi_cnt)) + "\n        multi_cnt_set: " + str(multi_cnt_set))
            for multi_cnt_item in multi_cnt_set:
                multi_cnt_items = [item for item in multi_cnt if item == multi_cnt_item]
                print("            num(" + str(multi_cnt_item) + "): "+ str(len(multi_cnt_items)))
            print("*******************************************")
            total_loss_cnt = sum(loss_cnt)
            loss_cnt_set = set(loss_cnt)
            print("Total loss cnt: " + str(total_loss_cnt) + ", total loss times: " + str(len(loss_cnt)) + "\n        loss_cnt_set: " + str(loss_cnt_set))
            for loss_cnt_item in loss_cnt_set:
                loss_cnt_items = [item for item in loss_cnt if item == loss_cnt_item]
                print("            num(" + str(loss_cnt_item) + "): "+ str(len(loss_cnt_items)))

if __name__ == "__main__":
    if len(sys.argv) == 2:
        loadradar(sys.argv[1])
    else:
        print("Usage: " + sys.argv[0] + " radar.txt")
