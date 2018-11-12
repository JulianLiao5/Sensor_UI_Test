#!/usr/bin/env python
# coding=utf-8

import inspect
import matplotlib.pyplot as plt
import numpy as np
import re
import sys

MINIMUM_DIST_Y = 3.45

def lineno():
    """Returns the current line number in our program."""
    return inspect.currentframe().f_back.f_lineno

def roundPartial(value, resolution):
    return round(value / resolution) * resolution

def loadradar(filename):
  lineno = 0
  distance_y = []
  dist_good_y = []
  dist_bad_y = []
  dist_bad_error_y = []

  bad_0_0_T_0_2 = []
  lineno_0_0_T_0_2 = []
  bad_0_2_T_0_4 = []
  lineno_0_2_T_0_4 = []
  bad_0_4_T_0_6 = []
  lineno_0_4_T_0_6 = []
  bad_0_6_T_0_8 = []
  lineno_0_6_T_0_8 = []
  bad_0_8_T_1_0 = []
  lineno_0_8_T_1_0 = []
  bad_1_0_T_1_5 = []
  lineno_1_0_T_1_5 = []
  bad_1_5_T_2_0 = []
  lineno_1_5_T_2_0 = []
  bad_great_than_2_0 = []
  lineno_great_than_2_0 = []
  with open(filename) as myfile:
    for line in myfile:
        if re.search("Angle", line, re.IGNORECASE):
            dist_y_name, dist_y_var = line.partition("distance_y: ")[::2]
            dist_y_item = dist_y_var.split(" ")[0]
            dist_y_val = float(dist_y_item)
            distance_y.append(dist_y_val)

            if dist_y_val >= MINIMUM_DIST_Y:
                dist_good_y.append(dist_y_val)
            else:
                dist_bad_y.append(dist_y_val)
                distance_error = MINIMUM_DIST_Y - dist_y_val
                dist_bad_error_y.append(distance_error)
                if distance_error <= 0.2:
                    bad_0_0_T_0_2.append(distance_error)
                    lineno_0_0_T_0_2.append(lineno)
                elif distance_error > 0.2 and distance_error <= 0.4:
                    bad_0_2_T_0_4.append(distance_error)
                    lineno_0_2_T_0_4.append(lineno)
                elif distance_error > 0.4 and distance_error <= 0.6:
                    bad_0_4_T_0_6.append(distance_error)
                    lineno_0_4_T_0_6.append(lineno)
                elif distance_error > 0.6 and distance_error <= 0.8:
                    bad_0_6_T_0_8.append(distance_error)
                    lineno_0_6_T_0_8.append(lineno)
                elif distance_error > 0.8 and distance_error <= 1.0:
                    bad_0_8_T_1_0.append(distance_error)
                    lineno_0_8_T_1_0.append(lineno)
                elif distance_error > 1.0 and distance_error <= 1.5:
                    bad_1_0_T_1_5.append(distance_error)
                    lineno_1_0_T_1_5.append(lineno)
                elif distance_error > 1.5 and distance_error <= 2.0:
                    bad_1_5_T_2_0.append(distance_error)
                    lineno_1_5_T_2_0.append(lineno)
                elif distance_error > 2.0:
                    bad_great_than_2_0.append(distance_error)
                    lineno_great_than_2_0.append(lineno)
            lineno = lineno + 1

  total_cnt = len(distance_y)
  bad_cnt = len(dist_bad_y)
  bad_rate = "{:.4%}".format(float(bad_cnt) / float(total_cnt))
  print("distance_y num: " + str(len(distance_y)) + " = " + str(len(dist_good_y)) + "[good]" + " + " + str(len(dist_bad_y)) + "[bad]")
  print("bad_rate: " + str(bad_rate))
  print("min: " + str(np.min(distance_y)) + ", min_bad: " + str(np.min(dist_bad_y)))
  print("dist_bad_error_y, min: " + "{0:.4f}".format(np.min(dist_bad_error_y)) + ", mean: " + "{0:.4f}".format(np.mean(dist_bad_error_y)) + ", max: " + "{0:.4f}".format(np.max(dist_bad_error_y)) + ", std dev: " + "{0:.4f}".format(np.std(dist_bad_error_y)))
  print("\n\n")
  
  bad_cnt_0_2 = len(bad_0_0_T_0_2)
  bad_cnt_0_4 = len(bad_0_2_T_0_4)
  bad_cnt_0_6 = len(bad_0_4_T_0_6)
  bad_cnt_0_8 = len(bad_0_6_T_0_8)
  bad_cnt_1_0 = len(bad_0_8_T_1_0)
  bad_cnt_1_5 = len(bad_1_0_T_1_5)
  bad_cnt_2_0 = len(bad_1_5_T_2_0)
  bad_cnt_gt_2 = len(bad_great_than_2_0)
  verify_bad_cnt = bad_cnt_0_2 + bad_cnt_0_4 + bad_cnt_0_6 + bad_cnt_0_8 + bad_cnt_1_0 + bad_cnt_1_5 + bad_cnt_2_0 + bad_cnt_gt_2
  print("bad_cnt:  " + str(bad_cnt) +
       "\n        bad_cnt_0_2:  " + str(bad_cnt_0_2) + "    ,    " + "{:.4%}".format(float(bad_cnt_0_2) / float(bad_cnt)) +
        "        |        " + str(lineno_0_0_T_0_2) + "    *    " + str(np.diff(lineno_0_0_T_0_2)) +
       "\n        bad_cnt_0_4:  " + str(bad_cnt_0_4) + "    ,    " + "{:.4%}".format(float(bad_cnt_0_4) / float(bad_cnt)) +
        "        |        " + str(lineno_0_2_T_0_4) + "    *    " + str(np.diff(lineno_0_2_T_0_4)) +
       "\n        bad_cnt_0_6:  " + str(bad_cnt_0_6) + "    ,    " + "{:.4%}".format(float(bad_cnt_0_6) / float(bad_cnt)) +
        "        |        " + str(lineno_0_4_T_0_6) + "    *    " + str(np.diff(lineno_0_4_T_0_6)) +
       "\n        bad_cnt_0_8:  " + str(bad_cnt_0_8) + "    ,    " + "{:.4%}".format(float(bad_cnt_0_8) / float(bad_cnt)) +
        "        |        " + str(lineno_0_6_T_0_8) + "    *    " + str(np.diff(lineno_0_6_T_0_8)) +
       "\n        bad_cnt_1_0:  " + str(bad_cnt_1_0) + "    ,    " + "{:.4%}".format(float(bad_cnt_1_0) / float(bad_cnt)) +
        "        |        " + str(lineno_0_8_T_1_0) + "    *    " + str(np.diff(lineno_0_8_T_1_0)) +
       "\n        bad_cnt_1_5:  " + str(bad_cnt_1_5) + "    ,    " + "{:.4%}".format(float(bad_cnt_1_5) / float(bad_cnt)) +
        "        |        " + str(lineno_1_0_T_1_5) + "    *    " + str(np.diff(lineno_1_0_T_1_5)) +
       "\n        bad_cnt_2_0:  " + str(bad_cnt_2_0) + "    ,    " + "{:.4%}".format(float(bad_cnt_2_0) / float(bad_cnt)) +
        "        |        " + str(lineno_1_5_T_2_0) + "    *    " + str(np.diff(lineno_1_5_T_2_0)) +
       "\n        bad_cnt_gt_2:  " + str(bad_cnt_gt_2) + "    ,    " + "{:.4%}".format(float(bad_cnt_gt_2) / float(bad_cnt)) +
        "        |        " + str(lineno_great_than_2_0) + "    *    " + str(np.diff(lineno_great_than_2_0)) +
       "\nverify_bad_cnt:  " + str(verify_bad_cnt)
       )
  return distance_y, dist_good_y, dist_bad_y, dist_bad_error_y

if __name__ == "__main__":
    if len(sys.argv) == 2:
        distance_y, dist_good_y, dist_bad_y, dist_bad_error_y = loadradar(sys.argv[1])
        fig = plt.figure("radar range in Y-axis")
        plt.plot(dist_bad_error_y)
        plt.ylabel('dist_bad_error_y')
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
