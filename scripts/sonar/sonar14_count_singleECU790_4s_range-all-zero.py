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
    return str(inspect.currentframe().f_back.f_lineno) + "  "

def roundPartial(value, resolution):
    return round(value / resolution) * resolution

def found790allzero(ts0, ts1, ts4, ts5):
    if ts0 > 0 and ts1 > 0 and ts4 > 0 and ts5 > 0 and ts0 == ts1 and ts1 == ts4 and ts4 == ts5:
      return True
    else:
      return False

def loadradar(filename):
    last_timestamp_val_0 = -1.0
    last_timestamp_val_1 = -1.0
    last_timestamp_val_4 = -1.0
    last_timestamp_val_5 = -1.0
    cnt_0 = 0
    cnt_1 = 0
    cnt_4 = 0
    cnt_5 = 0
    range_0 = []
    range_1 = []
    range_4 = []
    range_5 = []
    timestamp_0 = []
    timestamp_1 = []
    timestamp_4 = []
    timestamp_5 = []
    linux_timestamp_0 = []
    sonar_IDs = [0, 1, 4, 5]

    newest_0_range0_ts = -1
    newest_1_range0_ts = -1
    newest_4_range0_ts = -1
    newest_5_range0_ts = -1
    ts_790_all0_found = False
    ts_790_start = -1
    ts_790_end = -1
    CNT_allzero = 0
    ## 一定要有标记来表示本次全0是开始还是结束，不然没办法计算duration
    with open(filename) as myfile:
        with open('filter_sonar.txt', 'w+') as filter_file:
            for line in myfile:
                line = line[:-1]    # deletes extra line
                for aa in sonar_IDs:
                    if re.search("sonar_obj" + str(aa), line, re.IGNORECASE):
                        name, var = line.partition("Range: ")[::2]
                        range_item = var.split(" ")[0]
                        try:
                            range_val = float(range_item)
                        except:
                            print("BAD range: " + range_item + " bad")
                        name, var = line.partition("timestamp: ")[::2]
                        timestamp_item = var.split(" ")[0]
                        try:
                            timestamp_val = float(timestamp_item)
                        except:
                            print("BAD timestamp: " + timestamp_item + " bad")

                        range_valid = True 

                        if 0 == aa:
                            diff_timestamp_0 = timestamp_val - last_timestamp_val_0
                            if last_timestamp_val_0 >= 0.0 and 0 == diff_timestamp_0:
                                continue
                            last_timestamp_val_0 = timestamp_val
                            
                            timestamp_0.append(timestamp_val)
                            if 0 == range_val:
                                cnt_0 = cnt_0 + 1
                                newest_0_range0_ts = timestamp_val
                                if found790allzero(newest_0_range0_ts, newest_1_range0_ts, newest_4_range0_ts, newest_5_range0_ts):
                                    if ts_790_all0_found:
                                        print(lineno() + "790 has already been found, possible this is the END flag of 790!\n")
                                        ts_790_end = newest_0_range0_ts
                                        print(lineno() + "update ts_790_end: " + str(ts_790_end))
                                    else:
                                        ts_790_all0_found = True  ## 全新一次找到790
                                        ts_790_start = newest_0_range0_ts
                                        print("790 all-zero newly Found by 00!\n")
                            else:
                                if ts_790_end > 0:
                                    CNT_allzero += 1
                                    duration = ts_790_end - ts_790_start
                                    print(lineno() + "790 ONE loop END_in_00____-->" + str(CNT_allzero) + "<--ts_790: [" + str(ts_790_start) + ", " + str(ts_790_end) + "]  dura: " + str(duration) + "  RESET!!!\n")
                                    ts_790_all0_found = False
                                    ts_790_start = -1
                                    ts_790_end = -1

                            if range_valid:
                                range_0.append(range_val)
                        elif 1 == aa:
                            diff_timestamp_1 = timestamp_val - last_timestamp_val_1
                            if last_timestamp_val_1 >= 0.0 and 0 == diff_timestamp_1:
                                continue
                            last_timestamp_val_1 = timestamp_val

                            timestamp_1.append(timestamp_val)
                            if 0 == range_val:
                                cnt_1 = cnt_1 + 1
                                newest_1_range0_ts = timestamp_val
                                if found790allzero(newest_0_range0_ts, newest_1_range0_ts, newest_4_range0_ts, newest_5_range0_ts):
                                    if ts_790_all0_found:
                                        print(lineno() + "790 has already been found, possible this is the END flag of 790!\n")
                                        ts_790_end = newest_0_range0_ts
                                        print(lineno() + "update ts_790_end: " + str(ts_790_end))
                                    else:
                                        ts_790_all0_found = True  ## 全新一次找到790
                                        ts_790_start = newest_0_range0_ts
                                        print("790 all-zero newly Found by 11!\n")
                            else:
                                if ts_790_end > 0:
                                    CNT_allzero += 1
                                    duration = ts_790_end - ts_790_start
                                    print(lineno() + "790 ONE loop END_in_11____-->" + str(CNT_allzero) + "<--ts_790: [" + str(ts_790_start) + ", " + str(ts_790_end) + "]  dura: " + str(duration) + "  RESET!!!\n")
                                    ts_790_all0_found = False
                                    ts_790_start = -1
                                    ts_790_end = -1
                            if range_valid:
                                range_1.append(range_val)
                        elif 4 == aa:
                            diff_timestamp_4 = timestamp_val - last_timestamp_val_4
                            if last_timestamp_val_4 >= 0.0 and 0 == diff_timestamp_4:
                                continue
                            last_timestamp_val_4 = timestamp_val

                            timestamp_4.append(timestamp_val)
                            if 0 == range_val:
                                cnt_4 = cnt_4 + 1
                                newest_4_range0_ts = timestamp_val
                                if found790allzero(newest_0_range0_ts, newest_1_range0_ts, newest_4_range0_ts, newest_5_range0_ts):
                                    if ts_790_all0_found:
                                        print(lineno() + "790 has already been found, possible this is the END flag of 790!\n")
                                        ts_790_end = newest_0_range0_ts
                                        print(lineno() + "update ts_790_end: " + str(ts_790_end) + "\n")
                                    else:
                                        ts_790_all0_found = True  ## 全新一次找到790
                                        ts_790_start = newest_0_range0_ts
                                        print("790 all-zero newly Found by 44!\n")
                            else:
                                if ts_790_end > 0:
                                    CNT_allzero += 1
                                    duration = ts_790_end - ts_790_start
                                    print(lineno() + "790 ONE loop END_in_44____-->" + str(CNT_allzero) + "<--ts_790: [" + str(ts_790_start) + ", " + str(ts_790_end) + "]  dura: " + str(duration) + "  RESET!!!\n")
                                    ts_790_all0_found = False
                                    ts_790_start = -1
                                    ts_790_end = -1
                            if range_valid:
                                range_4.append(range_val)
                        elif 5 == aa:
                            diff_timestamp_5 = timestamp_val - last_timestamp_val_5
                            if last_timestamp_val_5 >= 0.0 and 0 == diff_timestamp_5:
                                continue
                            last_timestamp_val_5 = timestamp_val

                            timestamp_5.append(timestamp_val)
                            if 0 == range_val:
                                cnt_5 = cnt_5 + 1
                                newest_5_range0_ts = timestamp_val
                                if found790allzero(newest_0_range0_ts, newest_1_range0_ts, newest_4_range0_ts, newest_5_range0_ts):
                                    if ts_790_all0_found:
                                        print(lineno() + "790 has already been found, possible this is the END flag of 790!\n")
                                        ts_790_end = newest_0_range0_ts
                                        print(lineno() + "update ts_790_end: " + str(ts_790_end) + "\n")
                                    else:
                                        ts_790_all0_found = True  ## 全新一次找到790
                                        ts_790_start = newest_0_range0_ts
                                        print(lineno() + "790 all-zero newly Found by 55!  ts_790_start: " + str(ts_790_start) + "\n")
                            else:
                                if ts_790_end > 0:
                                    CNT_allzero += 1
                                    duration = ts_790_end - ts_790_start
                                    print(lineno() + "790 ONE loop END_in_55____-->" + str(CNT_allzero) + "<--ts_790: [" + str(ts_790_start) + ", " + str(ts_790_end) + "]  dura: " + str(duration) + "  RESET!!!\n")
                                    ts_790_all0_found = False
                                    ts_790_start = -1
                                    ts_790_end = -1
                            if range_valid:
                                range_5.append(range_val)

    return range_0, timestamp_0, cnt_0, range_1, timestamp_1, cnt_1, range_4, timestamp_4, cnt_4, range_5, timestamp_5, cnt_5

if __name__ == "__main__":
    if len(sys.argv) == 2:
        # frame_NO_0, range_0, timestamp_0, range_start_0, timestamp_start_0, range_end_0, timestamp_end_0, frame_NO_1, range_valid_1, timestamp_1, range_start_1, timestamp_start_1, range_end_1, timestamp_end_1 = loadradar(sys.argv[1])
        #  frame_NO_0, range_0, timestamp_0 = loadradar(sys.argv[1])
        range_0, ts_0, cnt_0, range_1, ts_1, cnt_1, range_4, ts_4, cnt_4, range_5, ts_5, cnt_5 = loadradar(sys.argv[1])
        ## print(timestamp_0)
        dt_0 = np.diff(ts_0)
        dt_1 = np.diff(ts_1)
        dt_4 = np.diff(ts_4)
        dt_5 = np.diff(ts_5)
        print("dt_0_len: " + str(len(dt_0)) + "\n"
              + "dt_1_len: " + str(len(dt_1)) + "\n"
              + "dt_4_len: " + str(len(dt_4)) + "\n"
              + "dt_5_len: " + str(len(dt_5)) + "\n"
             )
        duration_0 = ts_0[len(ts_0) - 1] - ts_0[0]
        min_0 = int(duration_0 / (1000 * 60))
        sec_0 = int((duration_0 - (min_0 * 1000 * 60)) / 1000)
        msec_0 = int((duration_0 - (min_0 * 1000 * 60)) % 1000)
        ## print(diff_time_0)
        figure1 = plt.figure("Sonar diff timestamp")
        font = {'family': 'serif',
                'color':  'blue',
                'weight': 'normal',
                'size': 16,
               }
        ax_dt_0 = figure1.add_subplot(4, 1, 1)
        ax_dt_0.plot(dt_0, '-b')
        curves = ["sonar0"]
        ax_dt_0.legend(curves, prop={'size':18})
        leg = ax_dt_0.get_legend()
        leg.legendHandles[0].set_color('blue')
        ax_dt_0.text(0.5, 0.5, "duration:    " + str(min_0) + "min : "  + str(sec_0) + "sec : " + str(msec_0) + "msec\n", horizontalalignment='center', verticalalignment='center', transform=ax_dt_0.transAxes, fontdict=font)
        ax_dt_0.grid(True)
        ax_dt_1 = figure1.add_subplot(4, 1, 2)
        ax_dt_1.plot(dt_1, '-b')
        curves = ["sonar1"]
        ax_dt_1.legend(curves, prop={'size':18})
        leg = ax_dt_1.get_legend()
        leg.legendHandles[0].set_color('blue')
        ax_dt_1.grid(True)
        ax_dt_4 = figure1.add_subplot(4, 1, 3)
        ax_dt_4.plot(dt_4, '-b')
        curves = ["sonar4"]
        ax_dt_4.legend(curves, prop={'size':18})
        leg = ax_dt_4.get_legend()
        leg.legendHandles[0].set_color('blue')
        ax_dt_4.grid(True)
        ax_dt_5 = figure1.add_subplot(4, 1, 4)
        ax_dt_5.plot(dt_5, '-b')
        curves = ["sonar5"]
        ax_dt_5.legend(curves, prop={'size':18})
        leg = ax_dt_5.get_legend()
        leg.legendHandles[0].set_color('blue')
        ax_dt_5.grid(True)
        ####################################################################################################################
        figure2 = plt.figure("Sonar Range")
        figure2.suptitle('Sonar Range Curve', x=0.50, y=0.96, fontsize=24)
        font = {'family': 'serif',
                'color':  'blue',
                'weight': 'normal',
                'size': 16,
               }
        ax_range_0 = figure2.add_subplot(4, 1, 1)
        ax_range_0.plot(range_0, '-r')
        curves = ["sonar0"]
        ax_range_0.legend(curves, prop={'size':18})
        leg = ax_range_0.get_legend()
        leg.legendHandles[0].set_color('blue')
        if 0 == len(range_0):
            ax_range_0.text(0.5, 0.5, 'range is empty', horizontalalignment='center', verticalalignment='center', transform=ax_range_0.transAxes, fontdict=font)
        else:
            ax_range_0.text(0.5, 0.5, "duration:    " + str(min_0) + "min : "  + str(sec_0) + "sec : " + str(msec_0) + "msec\n\n" + "CNT: " + str(len(range_0)) + "  CNT_0: " + str(cnt_0) + "\nmin: " + "{0:.1f}".format(np.min(range_0)) + "    mean: " + "{0:.1f}".format(np.mean(range_0)) + "    max: " + "{0:.1f}".format(np.max(range_0)), horizontalalignment='center', verticalalignment='center', transform=ax_range_0.transAxes, fontdict=font)
        ax_range_0.grid(True)
        ax_range_1 = figure2.add_subplot(4, 1, 2)
        ax_range_1.plot(range_1, '-r')
        curves = ["sonar1"]
        ax_range_1.legend(curves, prop={'size':18})
        leg = ax_range_1.get_legend()
        leg.legendHandles[0].set_color('blue')
        if 0 == len(range_1):
            ax_range_1.text(0.5, 0.5, 'range is empty', horizontalalignment='center', verticalalignment='center', transform=ax_range_1.transAxes, fontdict=font)
        else:
            ax_range_1.text(0.5, 0.5, "CNT: " + str(len(range_1)) + "  CNT_0: " + str(cnt_1) + "\nmin: " + "{0:.1f}".format(np.min(range_1)) + "    mean: " + "{0:.1f}".format(np.mean(range_1)) + "    max: " + "{0:.1f}".format(np.max(range_1)), horizontalalignment='center', verticalalignment='center', transform=ax_range_1.transAxes, fontdict=font)
        ax_range_1.grid(True)
        ax_range_4 = figure2.add_subplot(4, 1, 3)
        ax_range_4.plot(range_4, '-r')
        curves = ["sonar4"]
        ax_range_4.legend(curves, prop={'size':18})
        leg = ax_range_4.get_legend()
        leg.legendHandles[0].set_color('blue')
        if 0 == len(range_4):
            ax_range_4.text(0.5, 0.5, 'range is empty', horizontalalignment='center', verticalalignment='center', transform=ax_range_4.transAxes, fontdict=font)
        else:
            ax_range_4.text(0.5, 0.5, "CNT: " + str(len(range_4)) + "  CNT_0: " + str(cnt_4) + "\nmin: " + "{0:.1f}".format(np.min(range_4)) + "    mean: " + "{0:.1f}".format(np.mean(range_4)) + "    max: " + "{0:.1f}".format(np.max(range_4)), horizontalalignment='center', verticalalignment='center', transform=ax_range_4.transAxes, fontdict=font)
        ax_range_4.grid(True)
        ax_range_5 = figure2.add_subplot(4, 1, 4)
        ax_range_5.plot(range_5, '-r')
        curves = ["sonar5"]
        ax_range_5.legend(curves, prop={'size':18})
        leg = ax_range_5.get_legend()
        leg.legendHandles[0].set_color('blue')
        if 0 == len(range_5):
            ax_range_5.text(0.5, 0.5, 'range is empty', horizontalalignment='center', verticalalignment='center', transform=ax_range_5.transAxes, fontdict=font)
        else:
            ax_range_5.text(0.5, 0.5, "CNT: " + str(len(range_5)) + "  CNT_0: " + str(cnt_5) + "\nmin: " + "{0:.1f}".format(np.min(range_5)) + "    mean: " + "{0:.1f}".format(np.mean(range_5)) + "    max: " + "{0:.1f}".format(np.max(range_5)), horizontalalignment='center', verticalalignment='center', transform=ax_range_5.transAxes, fontdict=font)
        ax_range_5.grid(True)
        plt.show()
    else:
        print("Usage: " + sys.argv[0] + " radar.txt")
