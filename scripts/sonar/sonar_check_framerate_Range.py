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
    #  frame_num_0 = 0
    #  frame_num_1 = 0
    #  frame_num_2 = 0
    #  frame_num_3 = 0
    #  frame_num_4 = 0
    #  frame_num_5 = 0
    #  frame_num_6 = 0
    #  frame_num_7 = 0
    last_timestamp_val_0 = -1.0
    last_timestamp_val_1 = -1.0
    last_timestamp_val_2 = -1.0
    last_timestamp_val_3 = -1.0
    last_timestamp_val_4 = -1.0
    last_timestamp_val_5 = -1.0
    last_timestamp_val_6 = -1.0
    last_timestamp_val_7 = -1.0
    # NO_0 = []
    range_0 = []
    range_1 = []
    range_2 = []
    range_3 = []
    range_4 = []
    range_5 = []
    range_6 = []
    range_7 = []
    timestamp_0 = []
    timestamp_1 = []
    timestamp_2 = []
    timestamp_3 = []
    timestamp_4 = []
    timestamp_5 = []
    timestamp_6 = []
    timestamp_7 = []
    linux_timestamp_0 = []
    sonar_IDs = [0, 1, 2, 3, 4, 5, 6, 7]
    with open(filename) as myfile:
        with open('filter_sonar.txt', 'w+') as filter_file:
            for line in myfile:
                line = line[:-1]    # deletes extra line
                for aa in sonar_IDs:
                  if re.search("newestData_sonar" + str(aa), line, re.IGNORECASE):
                    name, var = line.partition("Range: ")[::2]
                    range_item = var.split(" ")[0]
                    range_val = float(range_item)
                    name, var = line.partition("timestamp: ")[::2]
                    timestamp_item = var.split(" ")[0]
                    timestamp_val = float(timestamp_item)

                    #if range_val_0 > 0 and range_val_0 < 60000:
                    range_val = 0.001 * range_val
                    if 0 == aa:
                        diff_timestamp_0 = timestamp_val - last_timestamp_val_0
                        if last_timestamp_val_0 >= 0.0 and 0 == diff_timestamp_0:
                                continue
                        ## print("frame_num_0: " + str(frame_num_0) + ", timestamp_val_0: " + str(timestamp_val_0) + ", last_timestamp_val_0: " + str(last_timestamp_val_0))
                        last_timestamp_val_0 = timestamp_val

                        range_0.append(range_val)
                        timestamp_0.append(timestamp_val)
                    elif 1 == aa:
                        diff_timestamp_1 = timestamp_val - last_timestamp_val_1
                        if last_timestamp_val_1 >= 0.0 and 0 == diff_timestamp_1:
                                continue
                        ## print("frame_num_0: " + str(frame_num_0) + ", timestamp_val_0: " + str(timestamp_val_0) + ", last_timestamp_val_0: " + str(last_timestamp_val_0))
                        last_timestamp_val_1 = timestamp_val

                        range_1.append(range_val)
                    elif 2 == aa:
                        diff_timestamp_2 = timestamp_val - last_timestamp_val_2
                        if last_timestamp_val_2 >= 0.0 and 0 == diff_timestamp_2:
                                continue
                        ## print("frame_num_0: " + str(frame_num_0) + ", timestamp_val_0: " + str(timestamp_val_0) + ", last_timestamp_val_0: " + str(last_timestamp_val_0))
                        last_timestamp_val_2 = timestamp_val

                        range_2.append(range_val)
                        timestamp_2.append(timestamp_val)
                    elif 3 == aa:
                        diff_timestamp_3 = timestamp_val - last_timestamp_val_3
                        if last_timestamp_val_3 >= 0.0 and 0 == diff_timestamp_3:
                                continue
                        ## print("frame_num_0: " + str(frame_num_0) + ", timestamp_val_0: " + str(timestamp_val_0) + ", last_timestamp_val_0: " + str(last_timestamp_val_0))
                        last_timestamp_val_3 = timestamp_val

                        range_3.append(range_val)
                        timestamp_3.append(timestamp_val)
                    elif 4 == aa:
                        diff_timestamp_4 = timestamp_val - last_timestamp_val_4
                        if last_timestamp_val_4 >= 0.0 and 0 == diff_timestamp_4:
                                continue
                        ## print("frame_num_0: " + str(frame_num_0) + ", timestamp_val_0: " + str(timestamp_val_0) + ", last_timestamp_val_0: " + str(last_timestamp_val_0))
                        last_timestamp_val_4 = timestamp_val

                        range_4.append(range_val)
                        timestamp_4.append(timestamp_val)
                    elif 5 == aa:
                        diff_timestamp_5 = timestamp_val - last_timestamp_val_5
                        if last_timestamp_val_5 >= 0.0 and 0 == diff_timestamp_5:
                                continue
                        ## print("frame_num_0: " + str(frame_num_0) + ", timestamp_val_0: " + str(timestamp_val_0) + ", last_timestamp_val_0: " + str(last_timestamp_val_0))
                        last_timestamp_val_5 = timestamp_val

                        range_5.append(range_val)
                        timestamp_5.append(timestamp_val)
                    elif 6 == aa:
                        diff_timestamp_6 = timestamp_val - last_timestamp_val_6
                        if last_timestamp_val_6 >= 0.0 and 0 == diff_timestamp_6:
                                continue
                        ## print("frame_num_0: " + str(frame_num_0) + ", timestamp_val_0: " + str(timestamp_val_0) + ", last_timestamp_val_0: " + str(last_timestamp_val_0))
                        last_timestamp_val_6 = timestamp_val

                        range_6.append(range_val)
                        timestamp_6.append(timestamp_val)
                    elif 7 == aa:
                        diff_timestamp_7 = timestamp_val - last_timestamp_val_7
                        if last_timestamp_val_7 >= 0.0 and 0 == diff_timestamp_7:
                                continue
                        ## print("frame_num_0: " + str(frame_num_0) + ", timestamp_val_0: " + str(timestamp_val_0) + ", last_timestamp_val_0: " + str(last_timestamp_val_0))
                        last_timestamp_val_7 = timestamp_val

                        range_7.append(range_val)
                        timestamp_7.append(timestamp_val)
                    np.savetxt(filter_file, np.array(line).reshape(1), fmt="%s")

    return range_0, timestamp_0, range_1, timestamp_1, range_2, timestamp_2, range_3, timestamp_3, range_4, timestamp_4, range_5, timestamp_5, range_6, timestamp_6, range_7, timestamp_7

if __name__ == "__main__":
    if len(sys.argv) == 2:
        # frame_NO_0, range_0, timestamp_0, range_start_0, timestamp_start_0, range_end_0, timestamp_end_0, frame_NO_1, range_valid_1, timestamp_1, range_start_1, timestamp_start_1, range_end_1, timestamp_end_1 = loadradar(sys.argv[1])
        #  frame_NO_0, range_0, timestamp_0 = loadradar(sys.argv[1])
        range_0, timestamp_0, range_1, timestamp_1, range_2, timestamp_2, range_3, timestamp_3, range_4, timestamp_4, range_5, timestamp_5, range_6, timestamp_6, range_7, timestamp_7  = loadradar(sys.argv[1])
        ## print(timestamp_0)
        diff_time_0 = np.diff(timestamp_0)
        diff_time_2 = np.diff(timestamp_2)
        diff_time_4 = np.diff(timestamp_4)
        diff_time_6 = np.diff(timestamp_6)
        duration_0 = timestamp_0[len(timestamp_0) - 1] - timestamp_0[0]
        min_0 = int(duration_0 / (1000 * 60))
        sec_0 = int((duration_0 - (min * 1000 * 60)) / 1000)
        msec_0 = int((duration_0 - (min * 1000 * 60)) % 1000)
        ## print(diff_time_0)
        figure1 = plt.figure("ID0 diff timestamp")
        font = {'family': 'serif',
                'color':  'blue',
                'weight': 'normal',
                'size': 16,
               }
        ax_1 = figure1.add_subplot(2, 2, 1)
        ax_1.plot(diff_time_0, '-b')
        ax_1.grid(True)
        ax_1.text(0, 90, "duration:    " + str(min) + "min : "  + str(sec) + "sec : " + str(msec) + "msec\n", fontdict=font)
        ax_1.text(750, 110, "ID0 - diff_time:\n        min: " + "{0:.2f}".format(np.min(diff_time_0)) + "ms\n        mean: " + "{0:.2f}".format(np.mean(diff_time_0)) + "ms\n        max: " + "{0:.2f}".format(np.max(diff_time_0)) + "ms\n        std dev: " + "{0:.2f}".format(np.std(diff_time_0)), fontdict=font)
        curves = ["CHANNEL1 - ID0 diff_time"]
        plt.legend(curves, prop={'size':18})
        leg = ax_1.get_legend()
        leg.legendHandles[0].set_color('blue')
        ax_2 = figure1.add_subplot(2, 2, 2)
        ax_2.plot(diff_time_2, '-g')
        ax_2.grid(True)
        ax_2.text(0, 90, "duration:    " + str(min) + "min : "  + str(sec) + "sec : " + str(msec) + "msec\n", fontdict=font)
        ax_2.text(750, 110, "ID0 - diff_time:\n        min: " + "{0:.2f}".format(np.min(diff_time_0)) + "ms\n        mean: " + "{0:.2f}".format(np.mean(diff_time_0)) + "ms\n        max: " + "{0:.2f}".format(np.max(diff_time_0)) + "ms\n        std dev: " + "{0:.2f}".format(np.std(diff_time_0)), fontdict=font)
        curves = ["CHANNEL1 - ID2 diff_time"]
        plt.legend(curves, prop={'size':18})
        leg = ax_2.get_legend()
        leg.legendHandles[0].set_color('blue')
        ax_3 = figure1.add_subplot(2, 2, 3)
        ax_3.plot(diff_time_4, '-r')
        ax_3.grid(True)
        ax_3.text(0, 90, "duration:    " + str(min) + "min : "  + str(sec) + "sec : " + str(msec) + "msec\n", fontdict=font)
        ax_3.text(750, 110, "ID0 - diff_time:\n        min: " + "{0:.2f}".format(np.min(diff_time_0)) + "ms\n        mean: " + "{0:.2f}".format(np.mean(diff_time_0)) + "ms\n        max: " + "{0:.2f}".format(np.max(diff_time_0)) + "ms\n        std dev: " + "{0:.2f}".format(np.std(diff_time_0)), fontdict=font)
        curves = ["CHANNEL1 - ID4 diff_time"]
        plt.legend(curves, prop={'size':18})
        leg = ax_3.get_legend()
        leg.legendHandles[0].set_color('blue')
        ax_4 = figure1.add_subplot(2, 2, 4)
        ax_4.plot(diff_time_6, '-m')
        ax_4.grid(True)
        print("len_Range: " + str(len(range_0)) + "        len_diff_time: " + str(len(diff_time_0)))
        font = {'family': 'serif',
                'color':  'blue',
                'weight': 'normal',
                'size': 16,
               }
        plt.text(0, 90, "duration:    " + str(min) + "min : "  + str(sec) + "sec : " + str(msec) + "msec\n", fontdict=font)
        plt.text(750, 110, "ID0 - diff_time:\n        min: " + "{0:.2f}".format(np.min(diff_time_0)) + "ms\n        mean: " + "{0:.2f}".format(np.mean(diff_time_0)) + "ms\n        max: " + "{0:.2f}".format(np.max(diff_time_0)) + "ms\n        std dev: " + "{0:.2f}".format(np.std(diff_time_0)), fontdict=font)
        plt.ylabel('ID0 diff timestamp[milliseconds]', size=10)
        plt.grid(True)
        fig2 = plt.figure("ID0 Range")
        plt.plot(range_0, '-r')
        font = {'family': 'serif',
                'color':  'blue',
                'weight': 'normal',
                'size': 16,
               }
        #plt.text(0, 90, "duration:    " + str(min) + "min : "  + str(sec) + "sec : " + str(msec) + "msec\n", fontdict=font)
        #plt.text(750, 110, "ID0 - diff_time:\n        min: " + "{0:.2f}".format(np.min(diff_time_0)) + "ms\n        mean: " + "{0:.2f}".format(np.mean(diff_time_0)) + "ms\n        max: " + "{0:.2f}".format(np.max(diff_time_0)) + "ms\n        std dev: " + "{0:.2f}".format(np.std(diff_time_0)), fontdict=font)
        #plt.ylabel('ID0 diff timestamp[milliseconds]', size=10)
        ## curves = ["CHANNEL0  -  CAN diff time"]
        ## plt.legend(curves, prop={'size':18})
        ## ax = plt.gca()
        ## leg = ax.get_legend()
        ## leg.legendHandles[0].set_color('blue')
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
