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
    init_0 = 1
    init_1 = 1
    frame_num_0 = 0
    frame_num_1 = 0
    last_timestamp_val_0 = -1.0
    last_timestamp_val_1 = -1.0
    NO_0 = []
    NO_1 = []
    range_0 = []
    timestamp_0 = []
    range_1 = []
    timestamp_1 = []
    range_start_0 = []
    timestamp_start_0 = []
    range_end_0 = []
    timestamp_end_0 = []
    range_start_1 = []
    timestamp_start_1 = []
    range_end_1 = []
    timestamp_end_1 = []
    with open(filename) as myfile:
        with open('filter_sonar.txt', 'w+') as filter_file:
            for line in myfile:
                line = line[:-1]    # deletes extra line
                # if re.search("buff[0]", line, re.IGNORECASE):
                if re.search("buff\[0\]", line, re.IGNORECASE):
                    name, var = line.partition("Range: ")[::2]
                    range_item_0 = var.split(" ")[0]
                    range_val_0 = float(range_item_0)
                    name, var = line.partition("timestamp: ")[::2]
                    timestamp_item_0 = var.split(" ")[0]
                    timestamp_val_0 = float(timestamp_item_0)

                    if last_timestamp_val_0 < 0.0:
                        frame_num_0 += 1
                    diff_timestamp_0 = timestamp_val_0 - last_timestamp_val_0
                    if last_timestamp_val_0 >= 0.0:
                        if 0 == diff_timestamp_0:
                            continue
                        else:
                            frame_num_0 += 1
                    print("frame_num_0: " + str(frame_num_0) + ", timestamp_val_0: " + str(timestamp_val_0) + ", last_timestamp_val_0: " + str(last_timestamp_val_0))
                    last_timestamp_val_0 = timestamp_val_0

                    if range_val_0 > 0 and range_val_0 < 60000:
                        if 1 == init_0:
                            init_0 = 0
                            init_timestamp_0 = timestamp_val_0
                            print("INIT with timestamp_val_0: " + str(timestamp_val_0))
                            timestamp_val_0 = 0
                        else:
                            timestamp_val_0 = timestamp_val_0 - init_timestamp_0
                            range_val_0 = 0.001 * range_val_0
                            NO_0.append(frame_num_0)
                            range_0.append(range_val_0)
                            timestamp_0.append(timestamp_val_0)
                            line = line + ", frame_num_0: " + str(frame_num_0)
                            np.savetxt(filter_file, np.array(line).reshape(1), fmt="%s")
                            if timestamp_val_0 >= 1000 and timestamp_val_0 <= 7000:    # 3000ms = 3s
                              range_start_0.append(range_val_0)
                              timestamp_start_0.append(timestamp_val_0)
                            elif timestamp_val_0 >= 25000 and timestamp_val_0 <= 36000:    # 3000ms = 3s
                              range_end_0.append(range_val_0)
                              timestamp_end_0.append(timestamp_val_0)
                # elif re.search("buff[1]", line, re.IGNORECASE):
                elif re.search("buff\[1\]", line, re.IGNORECASE):
                    name, var = line.partition("Range: ")[::2]
                    range_item_1 = var.split(" ")[0]
                    range_val_1 = float(range_item_1)
                    name, var = line.partition("timestamp: ")[::2]
                    timestamp_item_1 = var.split(" ")[0]
                    timestamp_val_1 = float(timestamp_item_1)

                    if last_timestamp_val_1 < 0.0:
                        frame_num_1 += 1
                    diff_timestamp_1 = timestamp_val_1 - last_timestamp_val_1
                    if last_timestamp_val_1 >= 0.0:
                        if 0 == diff_timestamp_1:
                            continue
                        else:
                            frame_num_1 += 1
                    print("frame_num_1: " + str(frame_num_1) + ", timestamp_val_1: " + str(timestamp_val_1) + ", last_timestamp_val_1: " + str(last_timestamp_val_1))
                    last_timestamp_val_1 = timestamp_val_1

                    if range_val_1 > 0 and range_val_1 < 60000:
                        if 1 == init_1:
                            init_1 = 0
                            init_timestamp_1 = timestamp_val_1
                            print("INIT with timestamp_val: " + str(timestamp_val_1))
                            timestamp_val_1 = 0
                        else:
                            timestamp_val_1 = timestamp_val_1 - init_timestamp_1
                            range_val_1 = 0.001 * range_val_1
                            NO_1.append(frame_num_1)
                            range_1.append(range_val_1)
                            timestamp_1.append(timestamp_val_1)
                            line = line + ", frame_num_1: " + str(frame_num_1)
                            np.savetxt(filter_file, np.array(line).reshape(1), fmt="%s")
                            if timestamp_val_1 >= 1000 and timestamp_val_1 <= 7000:    # 3000ms = 3s
                                range_start_1.append(range_val_1)
                                timestamp_start_1.append(timestamp_val_1)
                            elif timestamp_val_1 >= 25000 and timestamp_val_1 <= 36000:    # 3000ms = 3s
                                range_end_1.append(range_val_1)
                                timestamp_end_1.append(timestamp_val_1)

    return NO_0, range_0, timestamp_0, range_start_0, timestamp_start_0, range_end_0, timestamp_end_0, NO_1, range_1, timestamp_1, range_start_1, timestamp_start_1, range_end_1, timestamp_end_1
    # return NO_0, range_0, timestamp_0, range_start_0, timestamp_start_0, range_end_0, timestamp_end_0

if __name__ == "__main__":
    if len(sys.argv) == 2:
        frame_NO_0, range_valid_0, timestamp_0, range_start_0, timestamp_start_0, range_end_0, timestamp_end_0, frame_NO_1, range_valid_1, timestamp_1, range_start_1, timestamp_start_1, range_end_1, timestamp_end_1 = loadradar(sys.argv[1])
        # frame_NO_0, range_valid_0, timestamp_0, range_start_0, timestamp_start_0, range_end_0, timestamp_end_0 = loadradar(sys.argv[1])
        print(timestamp_0)
        diff_time_0 = np.diff(timestamp_0)
        print(diff_time_0)
        fig1 = plt.figure("ID0 diff timestamp")
        plt.plot(diff_time_0, '-b')
        font = {'family': 'serif',
                'color':  'blue',
                'weight': 'normal',
                'size': 14,
               }
        plt.text(10, 6000, "ID0 - diff_time:\n        min: " + "{0:.4f}".format(np.min(diff_time_0)) + "ms\n        mean: " + "{0:.4f}".format(np.mean(diff_time_0)) + "ms\n        max: " + "{0:.4f}".format(np.max(diff_time_0)) + "ms\n        std dev: " + "{0:.4f}".format(np.std(diff_time_0)), fontdict=font)
        plt.ylabel('ID0 diff timestamp[milliseconds]', size=10)
        plt.grid(True)
        diff_time_1 = np.diff(timestamp_1)
        plt.plot(diff_time_1, '-r')
        font = {'family': 'serif',
        'color':  'red',
        'weight': 'normal',
        'size': 14,
        }
        plt.text(110, 6000, "ID1 - diff_time:\n        min: " + "{0:.4f}".format(np.min(diff_time_1)) + "ms\n        mean: " + "{0:.4f}".format(np.mean(diff_time_1)) + "ms\n        max: " + "{0:.4f}".format(np.max(diff_time_1)) + "ms\n        std dev: " + "{0:.4f}".format(np.std(diff_time_1)), fontdict=font)
        plt.ylabel('diff timestamp[milliseconds]', size=10)
        curves = ["ID0", "ID1"]
        plt.legend(curves, prop={'size':10})
        ax = plt.gca()
        leg = ax.get_legend()
        leg.legendHandles[0].set_color('blue')
        leg.legendHandles[1].set_color('red')
        plt.grid(True)
        fig2 = plt.figure("sonar range 0")
        if True:
            plt.plot(timestamp_0, range_valid_0, '-b')
            plt.xlabel('timestamp_0[millisecond]', size=10)
            plt.ylabel('range_0[meter]', size=10)
            font = {'family': 'serif',
                    'color':  'blue',
                    'weight': 'normal',
                    'size': 14,
                   }
            plt.text(0, 3.8, "min: " + str(np.min(range_valid_0)) + ", mean: " +
                     "{0:.4f}".format(np.mean(range_valid_0)) + ", max: " + str(np.max(range_valid_0)) + ", std dev: " + "{0:.4f}".format(np.std(range_valid_0)), fontdict=font)
            for i in range(0, len(range_valid_0)):
                if np.max(range_valid_0) == range_valid_0[i]:
                    font = {'family': 'serif',
                            'color':  'blue',
                            'weight': 'normal',
                            'size': 12,
                           }
                    plt.text(27000, 3.0, "frame_NO_1[" + str(i) + "] = "+ str(frame_NO_0[i]) + "\n        timestamp_0: " + str(timestamp_0[i]) + "\n        range_0: " + str(range_valid_0[i]), fontdict=font)
                    largest_range_ts_0 = timestamp_0[i]
                    break
        # plt.yticks(np.arange(roundPartial(np.min(distance), 0.5), roundPartial(np.max(distance), 0.5), 0.5))
        if False:
            font = {'family': 'serif',
                    'color':  'blue',
                    'weight': 'normal',
                    'size': 12,
                   }
            plt.text(-500, 1.25, "Ground truth: 1.0m\n    timestamp: [1000, 7000]\n    min: " + "{0:.4f}".format(np.min(range_start_0)) + ", mean: " +
                     "{0:.4f}".format(np.mean(range_start_0)) + ", max: " + "{0:.4f}".format(np.max(range_start_0)) + ", std dev: " + "{0:.4f}".format(np.std(range_start_0)) +
                     "\n    error: " + "{:.4%}".format((np.mean(range_start_0) - 1.0) / 1.0), fontdict=font)
            font = {'family': 'serif',
                    'color':  'blue',
                    'weight': 'normal',
                    'size': 12,
                   }
            plt.text(25000, 1.25, "Ground truth: 1.0m\n    timestamp: [25000, 36000]\n    min: " + "{0:.4f}".format(np.min(range_end_0)) + ", mean: " +
                     "{0:.4f}".format(np.mean(range_end_0)) + ", max: " + "{0:.4f}".format(np.max(range_end_0)) + ", std dev: " + "{0:.4f}".format(np.std(range_end_0)) +
                     "\n    error: " + "{:.4%}".format((np.mean(range_end_0) - 1.0) / 1.0), fontdict=font)
            font = {'family': 'serif',
                    'color':  'red',
                    'weight': 'normal',
                    'size': 12,
                   }
        if False:
            plt.plot(timestamp_1, range_valid_1, '-r')
            plt.xlabel('timestamp_1[millisecond]', size=10)
            plt.ylabel('range_1[meter]', size=10)
            font = {'family': 'serif',
                    'color':  'red',
                    'weight': 'normal',
                    'size': 14,
                   }
            plt.text(15000, 3.8, "min: " + str(np.min(range_valid_1)) + ", mean: " +
                     "{0:.4f}".format(np.mean(range_valid_1)) + ", max: " + str(np.max(range_valid_1)) + ", std dev: " + "{0:.4f}".format(np.std(range_valid_1)), fontdict=font)
            for i in range(0, len(range_valid_1)):
                if np.max(range_valid_1) == range_valid_1[i]:
                    font = {'family': 'serif',
                            'color':  'red',
                            'weight': 'normal',
                            'size': 12,
                           }
                    plt.text(7000, 2.0, "frame_NO_1[" + str(i) + "] = "+ str(frame_NO_1[i]) + "\n        timestamp_1: " + str(timestamp_1[i]) + "\n        range_1: " + str(range_valid_1[i]), fontdict=font)
                    largest_range_ts_1 = timestamp_1[i]
                    break
        if False:
            font = {'family': 'serif',
                    'color':  'red',
                    'weight': 'normal',
                    'size': 12,
                   }
            plt.text(-500, 0.85, "Ground truth: 1.0m\n    timestamp: [1000, 7000]\n    min: " + "{0:.4f}".format(np.min(range_start_1)) + ", mean: " +
                     "{0:.4f}".format(np.mean(range_start_1)) + ", max: " + "{0:.4f}".format(np.max(range_start_0)) + ", std dev: " + "{0:.4f}".format(np.std(range_start_0)) +
                     "\n    error: " + "{:.4%}".format((np.mean(range_start_0) - 1.0) / 1.0), fontdict=font)
            font = {'family': 'serif',
                    'color':  'red',
                    'weight': 'normal',
                    'size': 12,
                   }
            plt.text(25000, 0.85, "Ground truth: 1.0m\n    timestamp: [25000, 36000]\n    min: " + "{0:.4f}".format(np.min(range_end_1)) + ", mean: " +
                     "{0:.4f}".format(np.mean(range_end_1)) + ", max: " + "{0:.4f}".format(np.max(range_end_1)) + ", std dev: " + "{0:.4f}".format(np.std(range_end_1)) +
                     "\n    error: " + "{:.4%}".format((np.mean(range_end_1) - 1.0) / 1.0), fontdict=font)
        if False:
            curves = ["ID0", "ID1"]
            plt.legend(curves, prop={'size':10})
            ax = plt.gca()
            leg = ax.get_legend()
            leg.legendHandles[0].set_color('blue')
            leg.legendHandles[1].set_color('red')
        plt.grid(True)
        plt.show()
    else:
        print("Usage: " + sys.argv[0] + " radar.txt")
