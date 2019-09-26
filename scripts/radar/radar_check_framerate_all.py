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
    last_timestamp_val_0 = -1.0
    last_timestamp_val_1 = -1.0
    last_timestamp_val_2 = -1.0
    last_timestamp_val_3 = -1.0
    last_timestamp_val_4 = -1.0
    last_timestamp_val_5 = -1.0
    last_timestamp_val_6 = -1.0
    last_timestamp_val_7 = -1.0
    timestamp_0 = []
    timestamp_1 = []
    timestamp_2 = []
    timestamp_3 = []
    timestamp_4 = []
    timestamp_5 = []
    timestamp_6 = []
    timestamp_7 = []
    radar_IDs = [0, 1, 2, 3, 4, 5, 6, 7]
    with open(filename) as myfile:
            for line in myfile:
                line = line[:-1]    # deletes extra line
                for aa in radar_IDs:
                  if re.search("vehicle_coordinate " + str(aa), line, re.IGNORECASE):
                    fields = line.split(" ")

                    ## fields[8] -> CAN_time
                    ## fields[9] -> Linux_time
                    cur_time = float(fields[8])
                    if 0 == aa:
                        diff_time_0 = cur_time - last_timestamp_val_0
                        if last_timestamp_val_0 >= 0.0 and diff_time_0 <= 0:
                            continue
                        timestamp_0.append(cur_time)

                        last_timestamp_val_0 = cur_time
                    elif 1 == aa:
                        diff_time_1 = cur_time - last_timestamp_val_1
                        if last_timestamp_val_1 >= 0.0 and diff_time_1 <= 0:
                            continue
                        timestamp_1.append(cur_time)

                        last_timestamp_val_1 = cur_time
                    elif 2 == aa:
                        diff_time_2 = cur_time - last_timestamp_val_2
                        if last_timestamp_val_2 >= 0.0 and diff_time_2 <= 0:
                            continue
                        timestamp_2.append(cur_time)

                        last_timestamp_val_2 = cur_time
                    elif 3 == aa:
                        diff_time_3 = cur_time - last_timestamp_val_3
                        if last_timestamp_val_3 >= 0.0 and diff_time_3 <= 0:
                            continue
                        timestamp_3.append(cur_time)

                        last_timestamp_val_3 = cur_time
                    elif 4 == aa:
                        diff_time_4 = cur_time - last_timestamp_val_4
                        if last_timestamp_val_4 >= 0.0 and diff_time_4 <= 0:
                            continue
                        timestamp_4.append(cur_time)

                        last_timestamp_val_4 = cur_time
                    elif 5 == aa:
                        diff_time_5 = cur_time - last_timestamp_val_5
                        if last_timestamp_val_5 >= 0.0 and diff_time_5 <= 0:
                            continue
                        timestamp_5.append(cur_time)

                        last_timestamp_val_5 = cur_time
                    elif 6 == aa:
                        diff_time_6 = cur_time - last_timestamp_val_6
                        if last_timestamp_val_6 >= 0.0 and diff_time_6 <= 0:
                            continue
                        timestamp_6.append(cur_time)

                        last_timestamp_val_6 = cur_time
                    elif 7 == aa:
                        diff_time_7 = cur_time - last_timestamp_val_7
                        if last_timestamp_val_7 >= 0.0 and diff_time_7 <= 0:
                            continue
                        timestamp_7.append(cur_time)

                        last_timestamp_val_7 = cur_time

    return timestamp_0, timestamp_1, timestamp_2, timestamp_3, timestamp_4, timestamp_5, timestamp_6, timestamp_7

if __name__ == "__main__":
    if len(sys.argv) == 2:
        # frame_NO_0, range_valid_0, timestamp_0, range_start_0, timestamp_start_0, range_end_0, timestamp_end_0, frame_NO_1, range_valid_1, timestamp_1, range_start_1, timestamp_start_1, range_end_1, timestamp_end_1 = loadradar(sys.argv[1])
        timestamp_0, timestamp_1, timestamp_2, timestamp_3, timestamp_4, timestamp_5, timestamp_6, timestamp_7 = loadradar(sys.argv[1])
        ## print(timestamp_0)
        diff_time_0_origin = np.diff(timestamp_0)
        #diff_time_0 = diff_time_0_origin
        diff_time_0 = [x for x in diff_time_0_origin if x < 1000]
        ratio_0 = (len(diff_time_0_origin) - len(diff_time_0)) / len(diff_time_0_origin)
        diff_time_1_origin = np.diff(timestamp_1)
        #diff_time_1 = diff_time_1_origin
        diff_time_1 = [x for x in diff_time_1_origin if x < 1000]
        ratio_1 = (len(diff_time_1_origin) - len(diff_time_1)) / len(diff_time_1_origin)
        diff_time_2_origin = np.diff(timestamp_2)
        diff_time_2 = diff_time_2_origin
        diff_time_3_origin = np.diff(timestamp_3)
        diff_time_3 = diff_time_3_origin
        diff_time_4_origin = np.diff(timestamp_4)
        diff_time_4 = diff_time_4_origin
        diff_time_5_origin = np.diff(timestamp_5)
        diff_time_5 = diff_time_5_origin
        diff_time_6_origin = np.diff(timestamp_6)
        diff_time_6 = diff_time_6_origin
        diff_time_7_origin = np.diff(timestamp_7)
        diff_time_7 = diff_time_7_origin
        #diff_time_7 = diff_time_7_origin
        diff_time_7 = [x for x in diff_time_7_origin if x < 1000]
        ratio_7 = (len(diff_time_7_origin) - len(diff_time_7)) / len(diff_time_7_origin)
        duration_0 = timestamp_0[len(timestamp_0) - 1] - timestamp_0[0]
        min_0 = int(duration_0 / (1000 * 60))
        sec_0 = int((duration_0 - (min_0 * 1000 * 60)) / 1000)
        msec_0 = int((duration_0 - (min_0 * 1000 * 60)) % 1000)
        duration_1 = timestamp_1[len(timestamp_1) - 1] - timestamp_1[0]
        min_1 = int(duration_1 / (1000 * 60))
        sec_1 = int((duration_1 - (min_1 * 1000 * 60)) / 1000)
        msec_1 = int((duration_1 - (min_1 * 1000 * 60)) % 1000)
        duration_7 = timestamp_7[len(timestamp_7) - 1] - timestamp_7[0]
        min_7 = int(duration_7 / (1000 * 60))
        sec_7 = int((duration_7 - (min_7 * 1000 * 60)) / 1000)
        msec_7 = int((duration_7 - (min_7 * 1000 * 60)) % 1000)
        figure1 = plt.figure("Radar diff timestamp")
        figure1.suptitle('Radars timeout', x=0.50, y=0.96, fontsize=24)
        ax_1 = figure1.add_subplot(4, 2, 1)
        ax_1.plot(diff_time_0, '-b')
        font = {'family': 'serif',
                #'color':  'blue',
                'color':  'black',
                'weight': 'normal',
                'size': 16,
               }
        ax_1.text(0, 3000, "duration:    " + str(min_0) + "min : "  + str(sec_0) + "sec : " + str(msec_0) + "msec\n", fontdict=font)
        ax_1.text(10000, 70, "ID0 ratio: " + "{0:.2f}".format(ratio_0) + " diff_time:\n        min: " + "{0:.2f}".format(np.min(diff_time_0)) + "ms\n        mean: " + "{0:.2f}".format(np.mean(diff_time_0)) + "ms\n        max: " + "{0:.2f}".format(np.max(diff_time_0)) + "ms\n        std dev: " + "{0:.2f}".format(np.std(diff_time_0)), fontdict=font)
        #ax_1.set_ylabel('ID0 diff timestamp[milliseconds]', size=10)
        ax_1.grid(True)
        curves = ["ID0  -  CAN diff time"]
        ax_1.legend(curves, prop={'size':18})
        leg = ax_1.get_legend()
        leg.legendHandles[0].set_color('blue')
        ax_2 = figure1.add_subplot(4, 2, 2)
        ax_2.plot(diff_time_1, '-g')
        font = {'family': 'serif',
                #'color':  'green',
                'color':  'black',
                'weight': 'normal',
                'size': 16,
               }
        ax_2.text(0, 3000, "duration:    " + str(min_1) + "min : "  + str(sec_1) + "sec : " + str(msec_1) + "msec\n", fontdict=font)
        ax_2.text(10000, 70, "ID1 ratio: " + "{0:.2f}".format(ratio_1) + " - diff_time:\n        min: " + "{0:.2f}".format(np.min(diff_time_1)) + "ms\n        mean: " + "{0:.2f}".format(np.mean(diff_time_1)) + "ms\n        max: " + "{0:.2f}".format(np.max(diff_time_1)) + "ms\n        std dev: " + "{0:.2f}".format(np.std(diff_time_1)), fontdict=font)
        #ax_2.set_ylabel('ID1 diff timestamp[milliseconds]', size=10)
        ax_2.grid(True)
        curves = ["ID1  -  CAN diff time"]
        ax_2.legend(curves, prop={'size':18})
        leg = ax_2.get_legend()
        leg.legendHandles[0].set_color('green')
        ax_3 = figure1.add_subplot(4, 2, 3)
        ax_3.plot(diff_time_2, '-r')
        ax_3.grid(True)
        curves = ["ID2  -  CAN diff time"]
        ax_3.legend(curves, prop={'size':18})
        leg = ax_3.get_legend()
        leg.legendHandles[0].set_color('blue')
        ax_4 = figure1.add_subplot(4, 2, 4)
        ax_4.plot(diff_time_3, '-r')
        ax_4.grid(True)
        curves = ["ID3  -  CAN diff time"]
        ax_4.legend(curves, prop={'size':18})
        leg = ax_4.get_legend()
        leg.legendHandles[0].set_color('blue')
        ax_5 = figure1.add_subplot(4, 2, 5)
        ax_5.plot(diff_time_4, '-r')
        ax_5.grid(True)
        curves = ["ID4  -  CAN diff time"]
        ax_5.legend(curves, prop={'size':18})
        leg = ax_5.get_legend()
        leg.legendHandles[0].set_color('blue')
        ax_6 = figure1.add_subplot(4, 2, 6)
        ax_6.plot(diff_time_5, '-r')
        ax_6.grid(True)
        curves = ["ID5  -  CAN diff time"]
        ax_6.legend(curves, prop={'size':18})
        leg = ax_6.get_legend()
        leg.legendHandles[0].set_color('blue')
        ax_7 = figure1.add_subplot(4, 2, 7)
        ax_7.plot(diff_time_6, '-r')
        ax_7.grid(True)
        curves = ["ID6  -  CAN diff time"]
        ax_7.legend(curves, prop={'size':18})
        leg = ax_7.get_legend()
        leg.legendHandles[0].set_color('blue')
        ax_8 = figure1.add_subplot(4, 2, 8)
        ax_8.plot(diff_time_7, '-m')
        font = {'family': 'serif',
                #'color':  'magenta',
                'color':  'black',
                'weight': 'normal',
                'size': 16,
               }
        ax_8.text(0, 3000, "duration:    " + str(min_7) + "min : "  + str(sec_7) + "sec : " + str(msec_7) + "msec\n", fontdict=font)
        ax_8.text(10000, 70, "ID7 ratio: " + "{0:.2f}".format(ratio_7) + " diff_time:\n        min: " + "{0:.2f}".format(np.min(diff_time_7)) + "ms\n        mean: " + "{0:.2f}".format(np.mean(diff_time_7)) + "ms\n        max: " + "{0:.2f}".format(np.max(diff_time_7)) + "ms\n        std dev: " + "{0:.2f}".format(np.std(diff_time_7)), fontdict=font)
        #ax_8.set_ylabel('ID7 diff timestamp[milliseconds]', size=10)
        ax_8.grid(True)
        curves = ["ID7  -  CAN diff time"]
        ax_8.legend(curves, prop={'size':18})
        leg = ax_8.get_legend()
        leg.legendHandles[0].set_color('magenta')
        plt.show()
    else:
        print("Usage: " + sys.argv[0] + " radar.txt")
