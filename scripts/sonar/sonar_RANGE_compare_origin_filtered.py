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
    cnt_ffff_0 = 0
    cnt_ffff_1 = 0
    cnt_ffff_2 = 0
    cnt_ffff_3 = 0
    cnt_ffff_4 = 0
    cnt_ffff_5 = 0
    cnt_ffff_6 = 0
    cnt_ffff_7 = 0
    ran_ori_0 = []
    ran_ori_1 = []
    ran_ori_2 = []
    ran_ori_3 = []
    ran_ori_4 = []
    ran_ori_5 = []
    ran_ori_6 = []
    ran_ori_7 = []
    range_0 = []
    range_1 = []
    range_2 = []
    range_3 = []
    range_4 = []
    range_5 = []
    range_6 = []
    range_7 = []
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
    linux_timestamp_0 = []
    sonar_IDs = [0, 1, 2, 3, 4, 5, 6, 7]
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

                        range_valid = False 
                        if range_val >= 0 and range_val < 60000:
                            range_valid = True 
                            range_val = 0.001 * range_val

                        if 0 == aa:
                            diff_timestamp_0 = timestamp_val - last_timestamp_val_0
                            if last_timestamp_val_0 >= 0.0 and 0 == diff_timestamp_0:
                                continue
                            ## print("frame_num_0: " + str(frame_num_0) + ", timestamp_val_0: " + str(timestamp_val_0) + ", last_timestamp_val_0: " + str(last_timestamp_val_0))
                            last_timestamp_val_0 = timestamp_val
                            
                            timestamp_0.append(timestamp_val)
                            ran_ori_0.append(range_val)
                            if range_valid:
                                range_0.append(range_val)
                            else:
                                cnt_ffff_0 += 1
                        elif 1 == aa:
                            diff_timestamp_1 = timestamp_val - last_timestamp_val_1
                            if last_timestamp_val_1 >= 0.0 and 0 == diff_timestamp_1:
                                continue
                            ## print("frame_num_0: " + str(frame_num_0) + ", timestamp_val_0: " + str(timestamp_val_0) + ", last_timestamp_val_0: " + str(last_timestamp_val_0))
                            last_timestamp_val_1 = timestamp_val

                            timestamp_1.append(timestamp_val)
                            ran_ori_1.append(range_val)
                            if range_valid:
                                range_1.append(range_val)
                            else:
                                cnt_ffff_1 += 1
                        elif 2 == aa:
                            diff_timestamp_2 = timestamp_val - last_timestamp_val_2
                            if last_timestamp_val_2 >= 0.0 and 0 == diff_timestamp_2:
                                continue
                            ## print("frame_num_0: " + str(frame_num_0) + ", timestamp_val_0: " + str(timestamp_val_0) + ", last_timestamp_val_0: " + str(last_timestamp_val_0))
                            last_timestamp_val_2 = timestamp_val

                            timestamp_2.append(timestamp_val)
                            ran_ori_2.append(range_val)
                            if range_valid:
                                range_2.append(range_val)
                            else:
                                cnt_ffff_2 += 1
                        elif 3 == aa:
                            diff_timestamp_3 = timestamp_val - last_timestamp_val_3
                            if last_timestamp_val_3 >= 0.0 and 0 == diff_timestamp_3:
                                continue
                            ## print("frame_num_0: " + str(frame_num_0) + ", timestamp_val_0: " + str(timestamp_val_0) + ", last_timestamp_val_0: " + str(last_timestamp_val_0))
                            last_timestamp_val_3 = timestamp_val

                            timestamp_3.append(timestamp_val)
                            ran_ori_3.append(range_val)
                            if range_valid:
                                range_3.append(range_val)
                            else:
                                cnt_ffff_3 += 1
                        elif 4 == aa:
                            diff_timestamp_4 = timestamp_val - last_timestamp_val_4
                            if last_timestamp_val_4 >= 0.0 and 0 == diff_timestamp_4:
                                continue
                            ## print("frame_num_0: " + str(frame_num_0) + ", timestamp_val_0: " + str(timestamp_val_0) + ", last_timestamp_val_0: " + str(last_timestamp_val_0))
                            last_timestamp_val_4 = timestamp_val

                            timestamp_4.append(timestamp_val)
                            ran_ori_4.append(range_val)
                            if range_valid:
                                range_4.append(range_val)
                            else:
                                cnt_ffff_4 += 1
                        elif 5 == aa:
                            diff_timestamp_5 = timestamp_val - last_timestamp_val_5
                            if last_timestamp_val_5 >= 0.0 and 0 == diff_timestamp_5:
                                continue
                            ## print("frame_num_0: " + str(frame_num_0) + ", timestamp_val_0: " + str(timestamp_val_0) + ", last_timestamp_val_0: " + str(last_timestamp_val_0))
                            last_timestamp_val_5 = timestamp_val

                            timestamp_5.append(timestamp_val)
                            ran_ori_5.append(range_val)
                            if range_valid:
                                range_5.append(range_val)
                            else:
                                cnt_ffff_5 += 1
                        elif 6 == aa:
                            diff_timestamp_6 = timestamp_val - last_timestamp_val_6
                            if last_timestamp_val_6 >= 0.0 and 0 == diff_timestamp_6:
                                continue
                            ## print("frame_num_0: " + str(frame_num_0) + ", timestamp_val_0: " + str(timestamp_val_0) + ", last_timestamp_val_0: " + str(last_timestamp_val_0))
                            last_timestamp_val_6 = timestamp_val

                            timestamp_6.append(timestamp_val)
                            ran_ori_6.append(range_val)
                            if range_valid:
                                range_6.append(range_val)
                            else:
                                cnt_ffff_6 += 1
                        elif 7 == aa:
                            diff_timestamp_7 = timestamp_val - last_timestamp_val_7
                            if last_timestamp_val_7 >= 0.0 and 0 == diff_timestamp_7:
                                continue
                            ## print("frame_num_0: " + str(frame_num_0) + ", timestamp_val_0: " + str(timestamp_val_0) + ", last_timestamp_val_0: " + str(last_timestamp_val_0))
                            last_timestamp_val_7 = timestamp_val

                            timestamp_7.append(timestamp_val)
                            ran_ori_7.append(range_val)
                            if range_valid:
                                range_7.append(range_val)
                            else:
                                cnt_ffff_7 += 1

    print("cnt_0: " + str(cnt_ffff_0)
          + "\ncnt_1: " + str(cnt_ffff_1)
          + "\ncnt_2: " + str(cnt_ffff_2)
          + "\ncnt_3: " + str(cnt_ffff_3)
          + "\ncnt_4: " + str(cnt_ffff_4)
          + "\ncnt_5: " + str(cnt_ffff_5)
          + "\ncnt_6: " + str(cnt_ffff_6)
          + "\ncnt_7: " + str(cnt_ffff_7)
         )
    return range_0, ran_ori_0, timestamp_0, range_1, ran_ori_1, timestamp_1, range_2, ran_ori_2, timestamp_2, range_3, ran_ori_3, timestamp_3, range_4, ran_ori_4, timestamp_4, range_5, ran_ori_5, timestamp_5, range_6, ran_ori_6, timestamp_6, range_7, ran_ori_7, timestamp_7

if __name__ == "__main__":
    if len(sys.argv) == 2:
        # frame_NO_0, range_0, timestamp_0, range_start_0, timestamp_start_0, range_end_0, timestamp_end_0, frame_NO_1, range_valid_1, timestamp_1, range_start_1, timestamp_start_1, range_end_1, timestamp_end_1 = loadradar(sys.argv[1])
        #  frame_NO_0, range_0, timestamp_0 = loadradar(sys.argv[1])
        range_0, ran_ori_0, ts_0, range_1, ran_ori_1, ts_1, range_2, ran_ori_2, ts_2, range_3, ran_ori_3, ts_3, range_4, ran_ori_4, ts_4, range_5, ran_ori_5, ts_5, range_6, ran_ori_6, ts_6, range_7, ran_ori_7, ts_7  = loadradar(sys.argv[1])
        CNT_F_0 = len(ran_ori_0) - len(range_0)
        CNT_F_1 = len(ran_ori_1) - len(range_1)
        CNT_F_2 = len(ran_ori_2) - len(range_2)
        CNT_F_3 = len(ran_ori_3) - len(range_3)
        CNT_F_4 = len(ran_ori_4) - len(range_4)
        CNT_F_5 = len(ran_ori_5) - len(range_5)
        CNT_F_6 = len(ran_ori_6) - len(range_6)
        CNT_F_7 = len(ran_ori_7) - len(range_7)
        print("len_ran_ori_0: " + str(len(ran_ori_0)) + ", len_ts_0: " + str(len(ts_0)) + ", len_CNT_F_0: " + str(CNT_F_0))
        print("len_ran_ori_1: " + str(len(ran_ori_1)) + ", len_ts_1: " + str(len(ts_1)) + ", len_CNT_F_1: " + str(CNT_F_1))
        print("len_ran_ori_2: " + str(len(ran_ori_2)) + ", len_ts_2: " + str(len(ts_2)) + ", len_CNT_F_2: " + str(CNT_F_2))
        print("len_ran_ori_3: " + str(len(ran_ori_3)) + ", len_ts_3: " + str(len(ts_3)) + ", len_CNT_F_3: " + str(CNT_F_3))
        print("len_ran_ori_4: " + str(len(ran_ori_4)) + ", len_ts_4: " + str(len(ts_4)) + ", len_CNT_F_4: " + str(CNT_F_4))
        print("len_ran_ori_5: " + str(len(ran_ori_5)) + ", len_ts_5: " + str(len(ts_5)) + ", len_CNT_F_5: " + str(CNT_F_5))
        print("len_ran_ori_6: " + str(len(ran_ori_6)) + ", len_ts_6: " + str(len(ts_6)) + ", len_CNT_F_6: " + str(CNT_F_6))
        print("len_ran_ori_7: " + str(len(ran_ori_7)) + ", len_ts_7: " + str(len(ts_7)) + ", len_CNT_F_7: " + str(CNT_F_7))
        ## print(timestamp_0)
        dt_0 = np.diff(ts_0)
        dt_1 = np.diff(ts_1)
        dt_2 = np.diff(ts_2)
        dt_3 = np.diff(ts_3)
        dt_4 = np.diff(ts_4)
        dt_5 = np.diff(ts_5)
        dt_6 = np.diff(ts_6)
        dt_7 = np.diff(ts_7)
        print("dt_0_len: " + str(len(dt_0)) + "\n"
              + "dt_1_len: " + str(len(dt_1)) + "\n"
              + "dt_2_len: " + str(len(dt_2)) + "\n"
              + "dt_3_len: " + str(len(dt_3)) + "\n"
              + "dt_4_len: " + str(len(dt_4)) + "\n"
              + "dt_5_len: " + str(len(dt_5)) + "\n"
              + "dt_6_len: " + str(len(dt_6)) + "\n"
              + "dt_7_len: " + str(len(dt_7)) + "\n"
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
        ax_dt_0 = figure1.add_subplot(4, 2, 1)
        ax_dt_0.plot(dt_0, '-b')
        curves = ["sonar0"]
        ax_dt_0.legend(curves, prop={'size':18})
        leg = ax_dt_0.get_legend()
        leg.legendHandles[0].set_color('blue')
        ax_dt_0.text(0.5, 0.5, "duration:    " + str(min_0) + "min : "  + str(sec_0) + "sec : " + str(msec_0) + "msec\n", horizontalalignment='center', verticalalignment='center', transform=ax_dt_0.transAxes, fontdict=font)
        ax_dt_0.grid(True)
        ax_dt_1 = figure1.add_subplot(4, 2, 2)
        ax_dt_1.plot(dt_1, '-b')
        curves = ["sonar1"]
        ax_dt_1.legend(curves, prop={'size':18})
        leg = ax_dt_1.get_legend()
        leg.legendHandles[0].set_color('blue')
        ax_dt_1.grid(True)
        ax_dt_2 = figure1.add_subplot(4, 2, 3)
        ax_dt_2.plot(dt_2, '-b')
        curves = ["sonar2"]
        ax_dt_2.legend(curves, prop={'size':18})
        leg = ax_dt_2.get_legend()
        leg.legendHandles[0].set_color('blue')
        ax_dt_2.grid(True)
        ax_dt_3 = figure1.add_subplot(4, 2, 4)
        ax_dt_3.plot(dt_3, '-b')
        curves = ["sonar3"]
        ax_dt_3.legend(curves, prop={'size':18})
        leg = ax_dt_3.get_legend()
        leg.legendHandles[0].set_color('blue')
        ax_dt_3.grid(True)
        ax_dt_4 = figure1.add_subplot(4, 2, 5)
        ax_dt_4.plot(dt_4, '-b')
        curves = ["sonar4"]
        ax_dt_4.legend(curves, prop={'size':18})
        leg = ax_dt_4.get_legend()
        leg.legendHandles[0].set_color('blue')
        ax_dt_4.grid(True)
        ax_dt_5 = figure1.add_subplot(4, 2, 6)
        ax_dt_5.plot(dt_5, '-b')
        curves = ["sonar5"]
        ax_dt_5.legend(curves, prop={'size':18})
        leg = ax_dt_5.get_legend()
        leg.legendHandles[0].set_color('blue')
        ax_dt_5.grid(True)
        ax_dt_6 = figure1.add_subplot(4, 2, 7)
        ax_dt_6.plot(dt_6, '-b')
        curves = ["sonar6"]
        ax_dt_6.legend(curves, prop={'size':18})
        leg = ax_dt_6.get_legend()
        leg.legendHandles[0].set_color('blue')
        ax_dt_6.grid(True)
        ax_dt_7 = figure1.add_subplot(4, 2, 8)
        ax_dt_7.plot(dt_7, '-b')
        curves = ["sonar7"]
        ax_dt_7.legend(curves, prop={'size':18})
        leg = ax_dt_7.get_legend()
        leg.legendHandles[0].set_color('blue')
        ax_dt_7.grid(True)
        #        ax_1.text(0, 90, "duration:    " + str(min_0) + "min : "  + str(sec_0) + "sec : " + str(msec_0) + "msec\n", fontdict=font)
        #        ax_1.text(750, 110, "ID0 - diff_time:\n        min: " + "{0:.2f}".format(np.min(diff_time_0)) + "ms\n        mean: " + "{0:.2f}".format(np.mean(diff_time_0)) + "ms\n        max: " + "{0:.2f}".format(np.max(diff_time_0)) + "ms\n        std dev: " + "{0:.2f}".format(np.std(diff_time_0)), fontdict=font)
        #        curves = ["CHANNEL1 - ID0 diff_time"]
        #        plt.legend(curves, prop={'size':18})
        #        leg = ax_1.get_legend()
        #        leg.legendHandles[0].set_color('blue')
        #        ax_2 = figure1.add_subplot(4, 2, 2)
        #        ax_2.plot(diff_time_2, '-g')
        #        ax_2.grid(True)
        #        # ax_2.text(0, 90, "duration:    " + str(min) + "min : "  + str(sec) + "sec : " + str(msec) + "msec\n", fontdict=font)
        #        ax_2.text(750, 110, "ID0 - diff_time:\n        min: " + "{0:.2f}".format(np.min(diff_time_2)) + "ms\n        mean: " + "{0:.2f}".format(np.mean(diff_time_2)) + "ms\n        max: " + "{0:.2f}".format(np.max(diff_time_2)) + "ms", fontdict=font)
        #        curves = ["CHANNEL1 - ID2 diff_time"]
        #        plt.legend(curves, prop={'size':18})
        #        leg = ax_2.get_legend()
        #        leg.legendHandles[0].set_color('blue')
        #        ax_3 = figure1.add_subplot(2, 2, 3)
        #        ax_3.plot(diff_time_4, '-r')
        #        ax_3.grid(True)
        #        # ax_3.text(0, 90, "duration:    " + str(min) + "min : "  + str(sec) + "sec : " + str(msec) + "msec\n", fontdict=font)
        #        ax_3.text(750, 110, "ID0 - diff_time:\n        min: " + "{0:.2f}".format(np.min(diff_time_4)) + "ms\n        mean: " + "{0:.2f}".format(np.mean(diff_time_4)) + "ms\n        max: " + "{0:.2f}".format(np.max(diff_time_4)) + "ms\n", fontdict=font)
        #        curves = ["CHANNEL1 - ID4 diff_time"]
        #        plt.legend(curves, prop={'size':18})
        #        leg = ax_3.get_legend()
        #        leg.legendHandles[0].set_color('blue')
        #        ax_4 = figure1.add_subplot(2, 2, 4)
        #        ax_4.plot(diff_time_6, '-m')
        #        ax_4.grid(True)
        #        print("len_Range: " + str(len(range_0)) + "        len_diff_time: " + str(len(diff_time_0)))
        #        font = {'family': 'serif',
        #                'color':  'blue',
        #                'weight': 'normal',
        #                'size': 16,
        #               }
        #        # ax_4.text(0, 90, "duration:    " + str(min) + "min : "  + str(sec) + "sec : " + str(msec) + "msec\n", fontdict=font)
        #        ax_4.text(750, 110, "ID0 - diff_time:\n        min: " + "{0:.2f}".format(np.min(diff_time_6)) + "ms\n        mean: " + "{0:.2f}".format(np.mean(diff_time_6)) + "ms\n        max: " + "{0:.2f}".format(np.max(diff_time_6)) + "ms\n        std dev: " + "{0:.2f}".format(np.std(diff_time_6)), fontdict=font)
        #        plt.ylabel('ID0 diff timestamp[milliseconds]', size=10)
        #        plt.grid(True)
        figure2 = plt.figure("Sonar0/1/2/3 Range")
        figure2.suptitle("Sonar0/1/2/3 Range Curve\nduration:    " + str(min_0) + "min : "  + str(sec_0) + "sec : " + str(msec_0) + "msec", x=0.50, y=0.99, fontsize=24)
        font = {'family': 'serif',
                'color':  'blue',
                'weight': 'normal',
                'size': 16,
               }
        ## ----------------BEGIN 0 -------------------- ##
        ax_ran_ori_0 = figure2.add_subplot(2, 4, 1)
        ax_ran_ori_0.plot(ran_ori_0, '-r')
        curves = ["sonar0 - origin"]
        ax_ran_ori_0.legend(curves, prop={'size':18})
        leg = ax_ran_ori_0.get_legend()
        leg.legendHandles[0].set_color('blue')
        if 0 == len(ran_ori_0):
            ax_ran_ori_0.text(0.5, 0.5, 'range is empty', horizontalalignment='center', verticalalignment='center', transform=ax_ran_ori_0.transAxes, fontdict=font)
        else:
            ax_ran_ori_0.text(0.5, 0.9, "min: " + "{0:.1f}".format(np.min(ran_ori_0)) + "    mean: " + "{0:.1f}".format(np.mean(ran_ori_0)) + "    max: " + "{0:.1f}".format(np.max(ran_ori_0)), horizontalalignment='center', verticalalignment='center', transform=ax_ran_ori_0.transAxes, fontdict=font)
        ax_ran_ori_0.grid(True)
        ## ************** ##
        ax_range_0 = figure2.add_subplot(2, 4, 5)
        ax_range_0.plot(range_0, '-r')
        curves = ["sonar0 - no 65535"]
        ax_range_0.legend(curves, prop={'size':18})
        leg = ax_range_0.get_legend()
        leg.legendHandles[0].set_color('blue')
        if 0 == len(range_0):
            ax_range_0.text(0.5, 0.5, 'range is empty', horizontalalignment='center', verticalalignment='center', transform=ax_range_0.transAxes, fontdict=font)
        else:
            ax_range_0.text(0.5, 0.9, "min: " + "{0:.1f}".format(np.min(range_0)) + "    mean: " + "{0:.1f}".format(np.mean(range_0)) + "    max: " + "{0:.1f}".format(np.max(range_0)), horizontalalignment='center', verticalalignment='center', transform=ax_range_0.transAxes, fontdict=font)
        ax_range_0.grid(True)
        ## ----------------END 0 --------------------- ##
        ## ----------------BEGIN 1 -------------------- ##
        ax_ran_ori_1 = figure2.add_subplot(2, 4, 2)
        ax_ran_ori_1.plot(ran_ori_1, '-r')
        curves = ["sonar1 - origin"]
        ax_ran_ori_1.legend(curves, prop={'size':18})
        leg = ax_ran_ori_1.get_legend()
        leg.legendHandles[0].set_color('blue')
        if 0 == len(ran_ori_1):
            ax_ran_ori_1.text(0.5, 0.5, 'range is empty', horizontalalignment='center', verticalalignment='center', transform=ax_ran_ori_1.transAxes, fontdict=font)
        else:
            ax_ran_ori_1.text(0.5, 0.5, "min: " + "{0:.1f}".format(np.min(ran_ori_1)) + "    mean: " + "{0:.1f}".format(np.mean(ran_ori_1)) + "    max: " + "{0:.1f}".format(np.max(ran_ori_1)), horizontalalignment='center', verticalalignment='center', transform=ax_ran_ori_1.transAxes, fontdict=font)
        ax_ran_ori_1.grid(True)
        ## ************** ##
        ax_range_1 = figure2.add_subplot(2, 4, 6)
        ax_range_1.plot(range_1, '-r')
        curves = ["sonar1 - no 65535"]
        ax_range_1.legend(curves, prop={'size':18})
        leg = ax_range_1.get_legend()
        leg.legendHandles[0].set_color('blue')
        if 0 == len(range_1):
            ax_range_1.text(0.5, 0.5, 'range is empty', horizontalalignment='center', verticalalignment='center', transform=ax_range_1.transAxes, fontdict=font)
        else:
            ax_range_1.text(0.5, 0.5, "min: " + "{0:.1f}".format(np.min(range_1)) + "    mean: " + "{0:.1f}".format(np.mean(range_1)) + "    max: " + "{0:.1f}".format(np.max(range_1)), horizontalalignment='center', verticalalignment='center', transform=ax_range_1.transAxes, fontdict=font)
        ax_range_1.grid(True)
        ## ----------------END 1 --------------------- ##
        ## ----------------BEGIN 2 --------------------- ##
        ax_ran_ori_2 = figure2.add_subplot(2, 4, 3)
        ax_ran_ori_2.plot(ran_ori_2, '-r')
        curves = ["sonar2 - origin"]
        ax_ran_ori_2.legend(curves, prop={'size':18})
        leg = ax_ran_ori_2.get_legend()
        leg.legendHandles[0].set_color('blue')
        if 0 == len(ran_ori_2):
            ax_ran_ori_2.text(0.5, 0.5, 'range is empty', horizontalalignment='center', verticalalignment='center', transform=ax_ran_ori_2.transAxes, fontdict=font)
        else:
            ax_ran_ori_2.text(0.5, 0.9, "min: " + "{0:.1f}".format(np.min(ran_ori_2)) + "    mean: " + "{0:.1f}".format(np.mean(ran_ori_2)) + "    max: " + "{0:.1f}".format(np.max(ran_ori_2)), horizontalalignment='center', verticalalignment='center', transform=ax_ran_ori_2.transAxes, fontdict=font)
        ax_ran_ori_2.grid(True)
        ## ************** ##
        ax_range_2 = figure2.add_subplot(2, 4, 7)
        ax_range_2.plot(range_2, '-r')
        curves = ["sonar2 - no 65535"]
        ax_range_2.legend(curves, prop={'size':18})
        leg = ax_range_2.get_legend()
        leg.legendHandles[0].set_color('blue')
        if 0 == len(range_2):
            ax_range_2.text(0.5, 0.5, 'range is empty', horizontalalignment='center', verticalalignment='center', transform=ax_range_2.transAxes, fontdict=font)
        else:
            ax_range_2.text(0.5, 0.9, "min: " + "{0:.1f}".format(np.min(range_2)) + "    mean: " + "{0:.1f}".format(np.mean(range_2)) + "    max: " + "{0:.1f}".format(np.max(range_2)), horizontalalignment='center', verticalalignment='center', transform=ax_range_2.transAxes, fontdict=font)
        ax_range_2.grid(True)
        ## ----------------END 2 --------------------- ##
        ## ----------------BEGIN 3 --------------------- ##
        ax_ran_ori_3 = figure2.add_subplot(2, 4, 4)
        ax_ran_ori_3.plot(ran_ori_3, '-r')
        curves = ["sonar3 - origin"]
        ax_ran_ori_3.legend(curves, prop={'size':18})
        leg = ax_ran_ori_3.get_legend()
        leg.legendHandles[0].set_color('blue')
        if 0 == len(ran_ori_3):
            ax_ran_ori_3.text(0.5, 0.5, 'range is empty', horizontalalignment='center', verticalalignment='center', transform=ax_ran_ori_3.transAxes, fontdict=font)
        else:
            ax_ran_ori_3.text(0.5, 0.5, "min: " + "{0:.1f}".format(np.min(ran_ori_3)) + "    mean: " + "{0:.1f}".format(np.mean(ran_ori_3)) + "    max: " + "{0:.1f}".format(np.max(ran_ori_3)), horizontalalignment='center', verticalalignment='center', transform=ax_ran_ori_3.transAxes, fontdict=font)
        ax_ran_ori_3.grid(True)
        ## ************** ##
        ax_range_3 = figure2.add_subplot(2, 4, 8)
        ax_range_3.plot(range_3, '-r')
        curves = ["sonar3 - no 65535"]
        ax_range_3.legend(curves, prop={'size':18})
        leg = ax_range_3.get_legend()
        leg.legendHandles[0].set_color('blue')
        if 0 == len(range_3):
            ax_range_3.text(0.5, 0.5, 'range is empty', horizontalalignment='center', verticalalignment='center', transform=ax_range_3.transAxes, fontdict=font)
        else:
            ax_range_3.text(0.5, 0.5, "min: " + "{0:.1f}".format(np.min(range_3)) + "    mean: " + "{0:.1f}".format(np.mean(range_3)) + "    max: " + "{0:.1f}".format(np.max(range_3)), horizontalalignment='center', verticalalignment='center', transform=ax_range_3.transAxes, fontdict=font)
        ax_range_3.grid(True)
        ## ----------------END 3 --------------------- ##
        ## =============================================================================================================================== ##
        figure3 = plt.figure("Sonar4/5/6/7 Range")
        figure3.suptitle("Sonar4/5/6/7 Range Curve\nduration:    " + str(min_0) + "min : "  + str(sec_0) + "sec : " + str(msec_0) + "msec", x=0.50, y=0.99, fontsize=24)
        font = {'family': 'serif',
                'color':  'blue',
                'weight': 'normal',
                'size': 16,
               }
        ## ----------------BEGIN 4 -------------------- ##
        ax_ran_ori_4 = figure3.add_subplot(2, 4, 1)
        ax_ran_ori_4.plot(ran_ori_4, '-r')
        curves = ["sonar4 - origin"]
        ax_ran_ori_4.legend(curves, prop={'size':18})
        leg = ax_ran_ori_4.get_legend()
        leg.legendHandles[0].set_color('blue')
        if 0 == len(ran_ori_4):
            ax_ran_ori_4.text(0.5, 0.5, 'range is empty', horizontalalignment='center', verticalalignment='center', transform=ax_ran_ori_4.transAxes, fontdict=font)
        else:
            ax_ran_ori_4.text(0.5, 0.9, "min: " + "{0:.1f}".format(np.min(ran_ori_4)) + "    mean: " + "{0:.1f}".format(np.mean(ran_ori_4)) + "    max: " + "{0:.1f}".format(np.max(ran_ori_4)), horizontalalignment='center', verticalalignment='center', transform=ax_ran_ori_4.transAxes, fontdict=font)
        ax_ran_ori_4.grid(True)
        ## ************** ##
        ax_range_4 = figure3.add_subplot(2, 4, 5)
        ax_range_4.plot(range_4, '-r')
        curves = ["sonar4 - no 65535"]
        ax_range_4.legend(curves, prop={'size':18})
        leg = ax_range_4.get_legend()
        leg.legendHandles[0].set_color('blue')
        if 0 == len(range_4):
            ax_range_4.text(0.5, 0.5, 'range is empty', horizontalalignment='center', verticalalignment='center', transform=ax_range_4.transAxes, fontdict=font)
        else:
            ax_range_4.text(0.5, 0.9, "min: " + "{0:.1f}".format(np.min(range_4)) + "    mean: " + "{0:.1f}".format(np.mean(range_4)) + "    max: " + "{0:.1f}".format(np.max(range_4)), horizontalalignment='center', verticalalignment='center', transform=ax_range_4.transAxes, fontdict=font)
        ax_range_4.grid(True)
        ## ----------------END 4 --------------------- ##
        ## ----------------BEGIN 5 -------------------- ##
        ax_ran_ori_5 = figure3.add_subplot(2, 4, 2)
        ax_ran_ori_5.plot(ran_ori_5, '-r')
        curves = ["sonar5 - origin"]
        ax_ran_ori_5.legend(curves, prop={'size':18})
        leg = ax_ran_ori_5.get_legend()
        leg.legendHandles[0].set_color('blue')
        if 0 == len(ran_ori_5):
            ax_ran_ori_5.text(0.5, 0.5, 'range is empty', horizontalalignment='center', verticalalignment='center', transform=ax_ran_ori_5.transAxes, fontdict=font)
        else:
            ax_ran_ori_5.text(0.5, 0.1, "min: " + "{0:.1f}".format(np.min(ran_ori_5)) + "    mean: " + "{0:.1f}".format(np.mean(ran_ori_5)) + "    max: " + "{0:.1f}".format(np.max(ran_ori_5)), horizontalalignment='center', verticalalignment='center', transform=ax_ran_ori_5.transAxes, fontdict=font)
        ax_ran_ori_5.grid(True)
        ## ************** ##
        ax_range_5 = figure3.add_subplot(2, 4, 6)
        ax_range_5.plot(range_5, '-r')
        curves = ["sonar5 - no 65535"]
        ax_range_5.legend(curves, prop={'size':18})
        leg = ax_range_5.get_legend()
        leg.legendHandles[0].set_color('blue')
        if 0 == len(range_5):
            ax_range_5.text(0.5, 0.5, 'range is empty', horizontalalignment='center', verticalalignment='center', transform=ax_range_5.transAxes, fontdict=font)
        else:
            ax_range_5.text(0.5, 0.1, "min: " + "{0:.1f}".format(np.min(range_5)) + "    mean: " + "{0:.1f}".format(np.mean(range_5)) + "    max: " + "{0:.1f}".format(np.max(range_5)), horizontalalignment='center', verticalalignment='center', transform=ax_range_5.transAxes, fontdict=font)
        ax_range_5.grid(True)
        ## ----------------END 5 --------------------- ##
        ## ----------------BEGIN 6 -------------------- ##
        ax_ran_ori_6 = figure3.add_subplot(2, 4, 3)
        ax_ran_ori_6.plot(ran_ori_6, '-r')
        curves = ["sonar6 - origin"]
        ax_ran_ori_6.legend(curves, prop={'size':18})
        leg = ax_ran_ori_6.get_legend()
        leg.legendHandles[0].set_color('blue')
        if 0 == len(ran_ori_6):
            ax_ran_ori_6.text(0.5, 0.5, 'range is empty', horizontalalignment='center', verticalalignment='center', transform=ax_ran_ori_6.transAxes, fontdict=font)
        else:
            ax_ran_ori_6.text(0.5, 0.9, "min: " + "{0:.1f}".format(np.min(ran_ori_6)) + "    mean: " + "{0:.1f}".format(np.mean(ran_ori_6)) + "    max: " + "{0:.1f}".format(np.max(ran_ori_6)), horizontalalignment='center', verticalalignment='center', transform=ax_ran_ori_6.transAxes, fontdict=font)
        ax_ran_ori_6.grid(True)
        ## ************** ##
        ax_range_6 = figure3.add_subplot(2, 4, 7)
        ax_range_6.plot(range_6, '-r')
        curves = ["sonar6 - no 65535"]
        ax_range_6.legend(curves, prop={'size':18})
        leg = ax_range_6.get_legend()
        leg.legendHandles[0].set_color('blue')
        if 0 == len(range_6):
            ax_range_6.text(0.5, 0.5, 'range is empty', horizontalalignment='center', verticalalignment='center', transform=ax_range_6.transAxes, fontdict=font)
        else:
            ax_range_6.text(0.5, 0.9, "min: " + "{0:.1f}".format(np.min(range_6)) + "    mean: " + "{0:.1f}".format(np.mean(range_6)) + "    max: " + "{0:.1f}".format(np.max(range_6)), horizontalalignment='center', verticalalignment='center', transform=ax_range_6.transAxes, fontdict=font)
        ax_range_6.grid(True)
        ## ----------------END 6 --------------------- ##
        ## ----------------BEGIN 7 -------------------- ##
        ax_ran_ori_7 = figure3.add_subplot(2, 4, 4)
        ax_ran_ori_7.plot(ran_ori_7, '-r')
        curves = ["sonar7 - origin"]
        ax_ran_ori_7.legend(curves, prop={'size':18})
        leg = ax_ran_ori_7.get_legend()
        leg.legendHandles[0].set_color('blue')
        if 0 == len(ran_ori_7):
            ax_ran_ori_7.text(0.5, 0.5, 'range is empty', horizontalalignment='center', verticalalignment='center', transform=ax_ran_ori_7.transAxes, fontdict=font)
        else:
            ax_ran_ori_7.text(0.5, 0.5, "min: " + "{0:.1f}".format(np.min(ran_ori_7)) + "    mean: " + "{0:.1f}".format(np.mean(ran_ori_7)) + "    max: " + "{0:.1f}".format(np.max(ran_ori_7)), horizontalalignment='center', verticalalignment='center', transform=ax_ran_ori_7.transAxes, fontdict=font)
        ax_ran_ori_7.grid(True)
        ## ************** ##
        ax_range_7 = figure3.add_subplot(2, 4, 8)
        ax_range_7.plot(range_7, '-r')
        curves = ["sonar7 - no 65535"]
        ax_range_7.legend(curves, prop={'size':18})
        leg = ax_range_7.get_legend()
        leg.legendHandles[0].set_color('blue')
        if 0 == len(range_7):
            ax_range_7.text(0.5, 0.5, 'range is empty', horizontalalignment='center', verticalalignment='center', transform=ax_range_7.transAxes, fontdict=font)
        else:
            ax_range_7.text(0.5, 0.5, "min: " + "{0:.1f}".format(np.min(range_7)) + "    mean: " + "{0:.1f}".format(np.mean(range_7)) + "    max: " + "{0:.1f}".format(np.max(range_7)), horizontalalignment='center', verticalalignment='center', transform=ax_range_7.transAxes, fontdict=font)
        ax_range_7.grid(True)
        ## ----------------END 7 --------------------- ##
        # ax_3.text(0, 90, "duration:    " + str(min) + "min : "  + str(sec) + "sec : " + str(msec) + "msec\n", fontdict=font)
        # ax_3.text(750, 110, "ID0 - diff_time:\n        min: " + "{0:.1f}".format(np.min(diff_time_0)) + "ms\n        mean: " + "{0:.2f}".format(np.mean(diff_time_0)) + "ms\n        max: " + "{0:.2f}".format(np.max(diff_time_0)) + "ms\n        std dev: " + "{0:.2f}".format(np.std(diff_time_0)), fontdict=font)
        # curves = ["CHANNEL1 - ID4 diff_time"]
        # plt.legend(curves, prop={'size':18})
        # leg = ax_3.get_legend()
        # leg.legendHandles[0].set_color('blue')
        #plt.text(0, 90, "duration:    " + str(min) + "min : "  + str(sec) + "sec : " + str(msec) + "msec\n", fontdict=font)
        #plt.text(750, 110, "ID0 - diff_time:\n        min: " + "{0:.2f}".format(np.min(diff_time_0)) + "ms\n        mean: " + "{0:.2f}".format(np.mean(diff_time_0)) + "ms\n        max: " + "{0:.2f}".format(np.max(diff_time_0)) + "ms\n        std dev: " + "{0:.2f}".format(np.std(diff_time_0)), fontdict=font)
        #plt.ylabel('ID0 diff timestamp[milliseconds]', size=10)
        ## curves = ["CHANNEL0  -  CAN diff time"]
        ## plt.legend(curves, prop={'size':18})
        ## ax = plt.gca()
        ## leg = ax.get_legend()
        ## leg.legendHandles[0].set_color('blue')
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
