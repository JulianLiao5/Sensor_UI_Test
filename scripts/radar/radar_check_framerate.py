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
    frame_num_0 = 0
    last_timestamp_val_0 = -1.0
    NO_0 = []
    range_0 = []
    timestamp_0 = []
    linux_timestamp_0 = []
    with open(filename) as myfile:
        with open('filter_sonar.txt', 'w+') as filter_file:
            for line in myfile:
                line = line[:-1]    # deletes extra line
                if re.search("vehicle_coordinate 0", line, re.IGNORECASE):
                    fields = line.split(" ")
                    print("0: " + fields[0] + ", 1: " + fields[1] + ", 2: " + fields[2])

                    if last_timestamp_val_0 < 0.0:
                        frame_num_0 += 1
                    diff_timestamp_0 = timestamp_val_0 - last_timestamp_val_0
                    if last_timestamp_val_0 >= 0.0:
                        if 0 == diff_timestamp_0:
                            continue
                        else:
                            frame_num_0 += 1
                    ## print("frame_num_0: " + str(frame_num_0) + ", timestamp_val_0: " + str(timestamp_val_0) + ", last_timestamp_val_0: " + str(last_timestamp_val_0))
                    last_timestamp_val_0 = timestamp_val_0

                    #if range_val_0 > 0 and range_val_0 < 60000:
                    range_val_0 = 0.001 * range_val_0
                    NO_0.append(frame_num_0)
                    range_0.append(range_val_0)
                    timestamp_0.append(timestamp_val_0)
                    linux_timestamp_0.append(linux_timestamp_val_0)
                    line = line + ", frame_num_0: " + str(frame_num_0)
                    np.savetxt(filter_file, np.array(line).reshape(1), fmt="%s")

    return NO_0, range_0, timestamp_0, linux_timestamp_0

if __name__ == "__main__":
    if len(sys.argv) == 2:
        # frame_NO_0, range_valid_0, timestamp_0, range_start_0, timestamp_start_0, range_end_0, timestamp_end_0, frame_NO_1, range_valid_1, timestamp_1, range_start_1, timestamp_start_1, range_end_1, timestamp_end_1 = loadradar(sys.argv[1])
        frame_NO_0, range_valid_0, timestamp_0, linux_timestamp_0 = loadradar(sys.argv[1])
        ## print(timestamp_0)
        diff_time_0 = np.diff(timestamp_0)
        first_time = timestamp_0[0]
        last_time = timestamp_0[len(timestamp_0) - 1]
        duration = last_time - first_time
        min = int(duration / (1000 * 60))
        sec = int((duration - (min * 1000 * 60)) / 1000)
        msec = int((duration - (min * 1000 * 60)) % 1000)
        ## print(diff_time_0)
        fig1 = plt.figure("ID0 diff timestamp")
        plt.plot(diff_time_0, '-b')
        font = {'family': 'serif',
                'color':  'blue',
                'weight': 'normal',
                'size': 16,
               }
        plt.text(0, 90, "duration:    " + str(min) + "min : "  + str(sec) + "sec : " + str(msec) + "msec\n", fontdict=font)
        plt.text(750, 110, "ID0 - diff_time:\n        min: " + "{0:.2f}".format(np.min(diff_time_0)) + "ms\n        mean: " + "{0:.2f}".format(np.mean(diff_time_0)) + "ms\n        max: " + "{0:.2f}".format(np.max(diff_time_0)) + "ms\n        std dev: " + "{0:.2f}".format(np.std(diff_time_0)), fontdict=font)
        plt.ylabel('ID0 diff timestamp[milliseconds]', size=10)
        curves = ["CHANNEL0  -  CAN diff time"]
        plt.legend(curves, prop={'size':18})
        ax = plt.gca()
        leg = ax.get_legend()
        leg.legendHandles[0].set_color('blue')
        plt.grid(True)
##        diff_linux_time = np.diff(linux_timestamp_0)
##        plt.plot(diff_linux_time, '-r')
##        font = {'family': 'serif',
##        'color':  'red',
##        'weight': 'normal',
##        'size': 14,
##        }
##        plt.text(110, 6000, "ID1 - diff_linux_time:\n        min: " + "{0:.4f}".format(np.min(diff_linux_time)) + "ms\n        mean: " + "{0:.4f}".format(np.mean(diff_linux_time)) + "ms\n        max: " + "{0:.4f}".format(np.max(diff_linux_time)) + "ms\n        std dev: " + "{0:.4f}".format(np.std(diff_linux_time)), fontdict=font)
##        plt.ylabel('diff timestamp[milliseconds]', size=10)
##        curves = ["CAN time", "Linux time"]
##        plt.legend(curves, prop={'size':10})
##        ax = plt.gca()
##        leg = ax.get_legend()
##        leg.legendHandles[0].set_color('blue')
##        leg.legendHandles[1].set_color('red')
##        plt.grid(True)
        plt.show()
    else:
        print("Usage: " + sys.argv[0] + " radar.txt")
