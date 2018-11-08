#!/usr/bin/env python
# coding=utf-8

import inspect
import matplotlib.pyplot as plt
import numpy as np
import re
import sys

MINIMUM_DIST_Y = 1.44

def lineno():
    """Returns the current line number in our program."""
    return inspect.currentframe().f_back.f_lineno

def roundPartial(value, resolution):
    return round(value / resolution) * resolution

def loadradar(filename):
  distance = []
  distance_good = []
  distance_bad = []
  distance_bad_2 = []
  bad_0_0_T_0_2 = []
  bad_0_2_T_0_4 = []
  bad_0_4_T_0_6 = []
  bad_0_6_T_0_8 = []
  bad_0_8_T_1_0 = []
  bad_great_than_1_0 = []
  with open(filename) as myfile:
    for line in myfile:
            name, var = line.partition("distance_y: ")[::2]
            distance_item = var.split(" ")[0]
            distance_val = float(distance_item)
            distance.append(distance_val)
            if distance_val >= MINIMUM_DIST_Y:
                distance_good.append(distance_val)
            else:
                distance_bad.append(distance_val)
                distance_error = MINIMUM_DIST_Y - distance_val
                distance_bad_2.append(distance_error)
                if distance_error <= 0.2:
                    bad_0_0_T_0_2.append(distance_error)
                elif distance_error > 0.2 and distance_error <= 0.4:
                    bad_0_2_T_0_4.append(distance_error)
                elif distance_error > 0.4 and distance_error <= 0.6:
                    bad_0_4_T_0_6.append(distance_error)
                elif distance_error > 0.6 and distance_error <= 0.8:
                    bad_0_6_T_0_8.append(distance_error)
                elif distance_error > 0.8 and distance_error <= 1.0:
                    bad_0_8_T_1_0.append(distance_error)
                elif distance_error > 1.0:
                    bad_great_than_1_0.append(distance_error)

  total_cnt = len(distance)
  bad_cnt = len(distance_bad)
  bad_rate = "{:.4%}".format(float(bad_cnt) / float(total_cnt))
  print("distance_y num: " + str(len(distance)) + " = " + str(len(distance_good)) + "[good]" + " + " + str(len(distance_bad)) + "[bad]")
  print("bad_rate: " + str(bad_rate))
  print("min: " + str(np.min(distance)) + ", min_bad: " + str(np.min(distance_bad)))
  print("min_bad_2: " + "{0:.4f}".format(np.min(distance_bad_2)) + ", mean_bad_2: " + "{0:.4f}".format(np.mean(distance_bad_2)) + ", max_bad_2: " + "{0:.4f}".format(np.max(distance_bad_2)) + ", std dev: " + "{0:.4f}".format(np.std(distance_bad_2)))
  print("\n\n")
  
  total_bad_cnt = len(distance_bad_2)
  bad_cnt_0_2 = len(bad_0_0_T_0_2)
  bad_cnt_0_4 = len(bad_0_2_T_0_4)
  bad_cnt_0_6 = len(bad_0_4_T_0_6)
  bad_cnt_0_8 = len(bad_0_6_T_0_8)
  bad_cnt_1_0 = len(bad_0_8_T_1_0)
  bad_cnt_gt_1 = len(bad_great_than_1_0)
  verify_bad_cnt = bad_cnt_0_2 + bad_cnt_0_4 + bad_cnt_0_6 + bad_cnt_0_8 + bad_cnt_1_0 + bad_cnt_gt_1
  print("total_cnt:  " + str(total_bad_cnt) + 
       "\n        bad_cnt_0_2:  " + str(bad_cnt_0_2) + "    ,    " + "{:.4%}".format(float(bad_cnt_0_2) / float(total_bad_cnt)) +
       "\n        bad_cnt_0_4:  " + str(bad_cnt_0_4) + "    ,    " + "{:.4%}".format(float(bad_cnt_0_4) / float(total_bad_cnt)) +
       "\n        bad_cnt_0_6:  " + str(bad_cnt_0_6) + "    ,    " + "{:.4%}".format(float(bad_cnt_0_6) / float(total_bad_cnt)) +
       "\n        bad_cnt_0_8:  " + str(bad_cnt_0_8) + "    ,    " + "{:.4%}".format(float(bad_cnt_0_8) / float(total_bad_cnt)) +
       "\n        bad_cnt_1_0:  " + str(bad_cnt_1_0) + "    ,    " + "{:.4%}".format(float(bad_cnt_1_0) / float(total_bad_cnt)) +
       "\n        bad_cnt_gt_1:  " + str(bad_cnt_gt_1) + "    ,    " + "{:.4%}".format(float(bad_cnt_gt_1) / float(total_bad_cnt)) +
       "\nverify_bad_cnt:  " + str(verify_bad_cnt)
       )
  return distance, distance_good, distance_bad, distance_bad_2

if __name__ == "__main__":
    if len(sys.argv) == 2:
        distance, distance_good, distance_bad, distance_bad_2 = loadradar(sys.argv[1])
        fig = plt.figure("radar range in Y-axis")
        plt.plot(distance_bad_2)
        plt.ylabel('distance_bad_2')
        # plt.yticks(np.arange(int(np.min(distance)), int(np.max(distance)) + 1, 1))
        '''
        font = {'family': 'serif',
        'color':  'darkorchid',
        'weight': 'normal',
        'size': 14,
        }
        plt.text(200, 14.8, "Ground truth: suppose 15.0m\n    min: " + str(np.min(distance)) + ", mean: " +
                 "{0:.4f}".format(np.mean(distance)) + ", max: " + str(np.max(distance)) + ", std dev: " + "{0:.4f}".format(np.std(distance)) +
                 "\n    error: " + "{:.4%}".format((np.mean(distance) - 15.0) / 15.0), fontdict=font)
        '''
        plt.grid(True)
        plt.show()
    else:
        print("Usage: " + sys.argv[0] + " radar.txt")
