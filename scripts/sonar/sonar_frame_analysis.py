#!/usr/bin/env python
# coding=utf-8

import inspect
import matplotlib.pyplot as plt
import numpy as np
import re
import sys

START_MOVE_CONTINUE_NUM = 5
END_MOVE_CONTINUE_NUM = 5


def lineno():
    """Returns the current line number in our program."""
    return inspect.currentframe().f_back.f_lineno

def roundPartial(value, resolution):
    return round(value / resolution) * resolution

def loadradar(filename):
  init = 1
  frame_num = 0
  last_timestamp_val = -1.0
  NO = []
  range = []
  timestamp = []
  range_start = []
  timestamp_start = []
  range_end = []
  timestamp_end = []
  with open(filename) as myfile:
    with open('filter_sonar.txt', 'w+') as filter_file:
      for line in myfile:
          line = line[:-1]    # deletes extra line
          if re.search("Range", line, re.IGNORECASE):
                name, var = line.partition("Range: ")[::2]
                range_item = var.split(" ")[0]
                range_val = float(range_item)
                name, var = line.partition("timestamp: ")[::2]
                timestamp_item = var.split(" ")[0]
                timestamp_val = float(timestamp_item)

                if last_timestamp_val < 0.0:
                    frame_num += 1
                diff_timestamp = timestamp_val - last_timestamp_val
                if last_timestamp_val >= 0.0:
                    if 0 == diff_timestamp:
                        continue
                    else:
                        frame_num += 1
                #print("frame_num: " + str(frame_num) + ", timestamp_val: " + str(timestamp_val) + ", last_timestamp_val: " + str(last_timestamp_val))
                last_timestamp_val = timestamp_val

                if range_val > 0 and range_val < 60000:
                    if 1 == init:
                        init = 0
                        init_timestamp = timestamp_val
                        print("INIT with timestamp_val: " + str(timestamp_val))
                        timestamp_val = 0
                    else:
                        timestamp_val = timestamp_val - init_timestamp
                        range_val = 0.001 * range_val
                        NO.append(frame_num)
                        range.append(range_val)
                        timestamp.append(timestamp_val)
                        line = line + ", frame_num: " + str(frame_num)
                        np.savetxt(filter_file, np.array(line).reshape(1), fmt="%s")
                        if timestamp_val >= 2000 and timestamp_val <= 5000:
                            range_start.append(range_val)
                            timestamp_start.append(timestamp_val)

  return NO, range, init_timestamp, timestamp, range_start, timestamp_start

if __name__ == "__main__":
    if len(sys.argv) == 2:
        frame_NO, range_valid, init_ts, timestamp, range_start, timestamp_start = loadradar(sys.argv[1])
        diff_time = np.diff(timestamp)
        fig1 = plt.figure("diff timestamp")
        plt.plot(diff_time, '-b')
        font = {'family': 'serif',
        'color':  'darkorchid',
        'weight': 'normal',
        'size': 14,
        }
        plt.text(10, 6000, "diff_time -- min: " + "{0:.4f}".format(np.min(diff_time)) + "ms, mean: " +
                 "{0:.4f}".format(np.mean(diff_time)) + "ms, max: " + "{0:.4f}".format(np.max(diff_time)) + "ms, std dev: " + "{0:.4f}".format(np.std(diff_time)), fontdict=font)
        plt.ylabel('diff timestamp[milliseconds]', size=10)
        plt.grid(True)
        fig = plt.figure("sonar range")
        plt.plot(timestamp, range_valid, '-r')
        plt.xlabel('timestamp[millisecond]', size=10)
        plt.ylabel('range[meter]', size=10)
        font = {'family': 'serif',
        'color':  'darkorchid',
        'weight': 'normal',
        'size': 14,
        }
        plt.text(8500, 1.5, "min: " + str(np.min(range_valid)) + ", mean: " +
                 "{0:.4f}".format(np.mean(range_valid)) + ", max: " + str(np.max(range_valid)) + ", std dev: " + "{0:.4f}".format(np.std(range_valid)), fontdict=font)
        for i in range(0, len(range_valid)):
            if np.max(range_valid) == range_valid[i]:
                font = {'family': 'serif',
                'color':  'darkred',
                'weight': 'normal',
                'size': 12,
                }
                plt.text(3500, 2.2, "frame_NO[" + str(i) + "] = "+ str(frame_NO[i]) + "\n        timestamp: " + str(timestamp[i]) + " - [" + str(init_ts + timestamp[i]) + "]\n        range: " + str(range_valid[i]), fontdict=font)
                largest_range_ts = timestamp[i]
                frame_NO.pop(i)
                range_valid.pop(i)
                timestamp.pop(i)
                break
        for i in range(0, len(range_valid)):
            if np.max(range_valid) == range_valid[i]:
                print("second_largest: " + str(np.max(range_valid)))
                font = {'family': 'serif',
                'color':  'darkred',
                'weight': 'normal',
                'size': 12,
                }
                diff_1_2_ts = timestamp[i] - largest_range_ts
                plt.text(16000, 1.9, "frame_NO[" + str(i) + "] = "+ str(frame_NO[i]) + "\n        timestamp: " + str(timestamp[i])  + " - [" + str(init_ts + timestamp[i]) + "]\n        diff_1_2: " + str(diff_1_2_ts) + "\n        range: " + str(range_valid[i]), fontdict=font)
                break
        # plt.yticks(np.arange(roundPartial(np.min(distance), 0.5), roundPartial(np.max(distance), 0.5), 0.5))
        font = {'family': 'serif',
        'color':  'darkred',
        'weight': 'normal',
        'size': 12,
        }
        plt.text(0, 1.08, "Ground truth: 1.0m\n    timestamp: [2000, 5000]\n    min: " + str(np.min(range_start)) + ", mean: " +
                 "{0:.4f}".format(np.mean(range_start)) + ", max: " + str(np.max(range_start)) + ", std dev: " + "{0:.4f}".format(np.std(range_start)) +
                 "\n    error: " + "{:.4%}".format((np.mean(range_start) - 1.0) / 1.0), fontdict=font)
        plt.grid(True)
        plt.show()
    else:
        print("Usage: " + sys.argv[0] + " radar.txt")
