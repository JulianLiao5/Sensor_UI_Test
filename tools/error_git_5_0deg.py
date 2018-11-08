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
  distance_y = []
  dist_y_0_0_T_0_5 = []
  dist_y_0_5_T_1_0 = []
  dist_y_1_0_T_1_5 = []
  dist_y_1_5_T_2_0 = []
  dist_y_2_0_T_2_5 = []
  dist_y_2_5_T_3_0 = []
  dist_y_3_0_T_3_5 = []
  dist_y_3_5_T_4_0 = []
  dist_y_4_0_T_4_5 = []
  dist_y_4_5_T_5_0 = []
  with open(filename) as myfile:
    for line in myfile:
            dist_y_name, dist_y_var = line.partition("distance_y: ")[::2]
            dist_y_item = dist_y_var.split(" ")[0]
            dist_y_val = float(dist_y_item)
            distance_y.append(dist_y_val)
            if (dist_y_val >= -0.5 and dist_y_val < 0.0) or (dist_y_val >= 0.0 and dist_y_val < 0.5):
                dist_y_0_0_T_0_5.append(dist_y_var)
            elif (dist_y_val >= -1.0 and dist_y_val < -0.5) or (dist_y_val >= 0.5 and dist_y_val < 1.0):
                dist_y_0_5_T_1_0.append(dist_y_var)
            elif (dist_y_val >= -1.5 and dist_y_val < -1.0) or (dist_y_val >= 1.0 and dist_y_val < 1.5):
                dist_y_1_0_T_1_5.append(dist_y_val)
            elif (dist_y_val >= -2.0 and dist_y_val < -1.5) or (dist_y_val >= 1.5 and dist_y_val < 2.0):
                dist_y_1_5_T_2_0.append(dist_y_var)
            elif (dist_y_val >= -2.5 and dist_y_val < -2.0) or (dist_y_val >= 2.0 and dist_y_val < 2.5):
                dist_y_2_0_T_2_5.append(dist_y_val)
            elif (dist_y_val >= -3.0 and dist_y_val < -2.5) or (dist_y_val >= 2.5 and dist_y_val < 3.0):
                dist_y_2_5_T_3_0.append(dist_y_var)
            elif (dist_y_val >= -3.5 and dist_y_val < -3.0) or (dist_y_val >= 3.0 and dist_y_val < 3.5):
                dist_y_3_0_T_3_5.append(dist_y_val)
            elif (dist_y_val >= -4.0 and dist_y_val < -3.5) or (dist_y_val >= 3.5 and dist_y_val < 4.0):
                dist_y_3_5_T_4_0.append(dist_y_var)
            elif (dist_y_val >= -4.5 and dist_y_val < -4.0) or (dist_y_val >= 4.0 and dist_y_val < 4.5):
                dist_y_4_0_T_4_5.append(dist_y_val)
            elif (dist_y_val >= -5.0 and dist_y_val < -4.5) or (dist_y_val >= 4.5 and dist_y_val < 5.0):
                dist_y_4_5_T_5_0.append(dist_y_var)

#  total_cnt = len(distance)
#  bad_cnt = len(distance_bad)
#  bad_rate = "{:.4%}".format(float(bad_cnt) / float(total_cnt))
#  print("distance_y num: " + str(len(distance)) + " = " + str(len(distance_good)) + "[good]" + " + " + str(len(distance_bad)) + "[bad]")
#  print("bad_rate: " + str(bad_rate))
#  print("min: " + str(np.min(distance)) + ", min_bad: " + str(np.min(distance_bad)))
#  print("min_bad_2: " + "{0:.4f}".format(np.min(distance_bad_2)) + ", mean_bad_2: " + "{0:.4f}".format(np.mean(distance_bad_2)) + ", max_bad_2: " + "{0:.4f}".format(np.max(distance_bad_2)) + ", std dev: " + "{0:.4f}".format(np.std(distance_bad_2)))
#  print("\n\n")
  
  total_cnt = len(distance_y)
  cnt_0_5 = len(dist_y_0_0_T_0_5)
  cnt_1_0 = len(dist_y_0_5_T_1_0)
  cnt_1_5 = len(dist_y_1_0_T_1_5)
  cnt_2_0 = len(dist_y_1_5_T_2_0)
  cnt_2_5 = len(dist_y_2_0_T_2_5)
  cnt_3_0 = len(dist_y_2_5_T_3_0)
  cnt_3_5 = len(dist_y_3_0_T_3_5)
  cnt_4_0 = len(dist_y_3_5_T_4_0)
  cnt_4_5 = len(dist_y_4_0_T_4_5)
  cnt_5_0 = len(dist_y_4_5_T_5_0)
  verify_total_cnt = cnt_0_5 + cnt_1_0 + cnt_1_5 + cnt_2_0 + cnt_2_5 + cnt_3_0 + cnt_3_5 + cnt_4_0 + cnt_4_5 + cnt_5_0
  print("total_cnt:  " + str(total_cnt) + 
       "\n        cnt_0_5:  " + str(cnt_0_5) + "    ,    " + "{:.2%}".format(float(cnt_0_5) / float(total_cnt)) +
       "\n        cnt_1_0:  " + str(cnt_1_0) + "    ,    " + "{:.2%}".format(float(cnt_1_0) / float(total_cnt)) +
       "\n        cnt_1_5:  " + str(cnt_1_5) + "    ,    " + "{:.2%}".format(float(cnt_1_5) / float(total_cnt)) +
       "\n        cnt_2_0:  " + str(cnt_2_0) + "    ,    " + "{:.2%}".format(float(cnt_2_0) / float(total_cnt)) +
       "\n        cnt_2_5:  " + str(cnt_2_5) + "    ,    " + "{:.2%}".format(float(cnt_2_5) / float(total_cnt)) +
       "\n        cnt_3_0:  " + str(cnt_3_0) + "    ,    " + "{:.2%}".format(float(cnt_3_0) / float(total_cnt)) +
       "\n        cnt_3_5:  " + str(cnt_3_5) + "    ,    " + "{:.2%}".format(float(cnt_3_5) / float(total_cnt)) +
       "\n        cnt_4_0:  " + str(cnt_4_0) + "    ,    " + "{:.2%}".format(float(cnt_4_0) / float(total_cnt)) +
       "\n        cnt_4_5:  " + str(cnt_4_5) + "    ,    " + "{:.2%}".format(float(cnt_4_5) / float(total_cnt)) +
       "\n        cnt_5_0:  " + str(cnt_5_0) + "    ,    " + "{:.2%}".format(float(cnt_5_0) / float(total_cnt)) +
       "\nverify_total_cnt:  " + str(verify_total_cnt)
       )
  return distance_y

if __name__ == "__main__":
    if len(sys.argv) == 2:
        distance_y = loadradar(sys.argv[1])
        # fig = plt.figure("radar range in Y-axis")
        # plt.plot(distance_bad_2)
        # plt.ylabel('distance_bad_2')
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
