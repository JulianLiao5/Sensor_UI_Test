#!/usr/bin/env python
# coding=utf-8

import inspect
import matplotlib.pyplot as plt
import numpy as np
import re
import sys

START_MOVE_CONTINUE_NUM = 5
END_MOVE_CONTINUE_NUM = 5

# unit: ms
MAX_INTERVAL_BETWEEN_790_791 = 20
MAX_END_INTERVAL_BETWEEN_790_791 = 45 

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

def found791allzero(ts2, ts3, ts6, ts7):
    if ts2 > 0 and ts3 > 0 and ts6 > 0 and ts7 > 0 and ts2 == ts3 and ts3 == ts6 and ts6 == ts7:
      return True
    else:
      return False

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
    cnt_0 = 0
    cnt_1 = 0
    cnt_2 = 0
    cnt_3 = 0
    cnt_4 = 0
    cnt_5 = 0
    cnt_6 = 0
    cnt_7 = 0
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

    newest_0_range0_ts = -1
    newest_1_range0_ts = -1
    newest_4_range0_ts = -1
    newest_5_range0_ts = -1
    newest_2_range0_ts = -1
    newest_3_range0_ts = -1
    newest_6_range0_ts = -1
    newest_7_range0_ts = -1
    ts_790_all0_found = False
    ts_791_all0_found = False
    ts_790_start = -1
    ts_791_start = -1
    ts_790_end = -1
    ts_791_end = -1
    ts_790_791_START_matched = False
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
                        # if range_val >= 0 and range_val < 60000:
                        #     range_valid = True 
                        #     range_val = 0.001 * range_val

                        if 0 == aa:
                            diff_timestamp_0 = timestamp_val - last_timestamp_val_0
                            if last_timestamp_val_0 >= 0.0 and 0 == diff_timestamp_0:
                                continue
                            ## print("frame_num_0: " + str(frame_num_0) + ", timestamp_val_0: " + str(timestamp_val_0) + ", last_timestamp_val_0: " + str(last_timestamp_val_0))
                            last_timestamp_val_0 = timestamp_val
                            
                            timestamp_0.append(timestamp_val)
                            if 0 == range_val:
                                cnt_0 = cnt_0 + 1
                                newest_0_range0_ts = timestamp_val
                                if found790allzero(newest_0_range0_ts, newest_1_range0_ts, newest_4_range0_ts, newest_5_range0_ts):
                                    if ts_790_all0_found:
                                        print(lineno() + "790 has already been found, possible this is the END flag of 790!\n")
                                        if ts_790_791_START_matched:
                                            ts_790_end = newest_0_range0_ts
                                            print(lineno() + "790/791 has the same start, check the common end of them now....  ts_790_end: " + str(ts_790_end))
                                        else:
                                            print("Still need to search the common start of 790/791!\n")
                                            ts_790_start = newest_0_range0_ts
                                            if ts_791_all0_found:
                                                print("791 all-zero already Found!\n")
                                                if abs(ts_791_start - ts_790_start) <= MAX_INTERVAL_BETWEEN_790_791:
                                                    ts_790_791_START_matched = True
                                                    print(lineno() + "ALL-zero[BEGIN] found!!!!!!\n")
                                                else:
                                                    print("790_allzero doesn't MATCH 791_allzereo in timestamp: " + str(abs(ts_791_start - ts_790_start)) + ", wait for next all0 0f 790 to determine common start!\n")
                                            else:
                                                print(lineno() + "wait start of 790 all-zero to determine common start\n")
                                    else:
                                        ts_790_all0_found = True  ## 全新一次找到790
                                        ts_790_start = newest_0_range0_ts
                                        print("790 all-zero newly Found!\n")

                                        if ts_791_all0_found:
                                            print("791 all-zero already Found!\n")
                                            if abs(ts_791_start - ts_790_start) <= MAX_INTERVAL_BETWEEN_790_791:
                                                ts_790_791_START_matched = True
                                                print("ALL-zero[BEGIN] found!!!!!!\n")
                                            else:
                                                print("790_allzero doesn't MATCH 791_allzereo in timestamp: " + str(abs(ts_791_start - ts_790_start)) + ", wait for next all0 0f 791\n")
                                        else:
                                            print("wait start of 791 all-zero\n")
                            else:
                                if ts_790_791_START_matched and ts_791_end > 0 and ts_790_end > 0 and abs(ts_791_end - ts_790_end) <= MAX_END_INTERVAL_BETWEEN_790_791:
                                    print(lineno() + "found 790/791 common end, ONE loop END!!!!!!!!!!!!!!!!!  ts_790: [" + str(ts_790_start) + ", " + str(ts_790_end) + "]  ts_791: [" + str(ts_791_start) + ", " + str(ts_791_end) + "]\n")
                                    CNT_allzero += 1
                                    duration = (ts_790_end + ts_791_end) / 2 - (ts_790_start + ts_791_start) / 2
                                    ts_790_all0_found = False
                                    ts_790_start = -1
                                    ts_790_end = -1
                                    ts_791_all0_found = False
                                    ts_791_start = -1
                                    ts_791_end = -1
                                    ts_790_791_START_matched = False
                                    print("ALL-zero[END]" + str(CNT_allzero) + ", duration: " + str(duration) + "  RESET!!!\n")

                            if range_valid:
                                range_0.append(range_val)
                        elif 1 == aa:
                            diff_timestamp_1 = timestamp_val - last_timestamp_val_1
                            if last_timestamp_val_1 >= 0.0 and 0 == diff_timestamp_1:
                                continue
                            ## print("frame_num_0: " + str(frame_num_0) + ", timestamp_val_0: " + str(timestamp_val_0) + ", last_timestamp_val_0: " + str(last_timestamp_val_0))
                            last_timestamp_val_1 = timestamp_val

                            timestamp_1.append(timestamp_val)
                            if 0 == range_val:
                                cnt_1 = cnt_1 + 1
                                newest_1_range0_ts = timestamp_val
                                if found790allzero(newest_0_range0_ts, newest_1_range0_ts, newest_4_range0_ts, newest_5_range0_ts):
                                    if ts_790_all0_found:
                                        print(lineno() + "790 has already been found, possible this is the END flag of 790!\n")
                                        if ts_790_791_START_matched:
                                            ts_790_end = newest_0_range0_ts
                                            print(lineno() + "790/791 has the same start, check the common end of them now....  ts_790_end: " + str(ts_790_end))
                                        else:
                                            print("Still need to search the common start of 790/791!\n")
                                            ts_790_start = newest_0_range0_ts
                                            if ts_791_all0_found:
                                                print("791 all-zero already Found!\n")
                                                if abs(ts_791_start - ts_790_start) <= MAX_INTERVAL_BETWEEN_790_791:
                                                    ts_790_791_START_matched = True
                                                    print(lineno() + "ALL-zero[BEGIN] found!!!!!!\n")
                                                else:
                                                    print("790_allzero doesn't MATCH 791_allzereo in timestamp: " + str(abs(ts_791_start - ts_790_start)) + ", wait for next all0 0f 790 to determine common start!\n")
                                            else:
                                                print(lineno() + "wait start of 790 all-zero to determine common start\n")
                                    else:
                                        ts_790_all0_found = True  ## 全新一次找到790
                                        ts_790_start = newest_0_range0_ts
                                        print("790 all-zero newly Found!\n")

                                        if ts_791_all0_found:
                                            print("791 all-zero already Found!\n")
                                            if abs(ts_791_start - ts_790_start) <= MAX_INTERVAL_BETWEEN_790_791:
                                                ts_790_791_START_matched = True
                                                print("ALL-zero[BEGIN] found!!!!!!\n")
                                            else:
                                                print("790_allzero doesn't MATCH 791_allzereo in timestamp: " + str(abs(ts_791_start - ts_790_start)) + ", wait for next all0 0f 791\n")
                                        else:
                                            print("wait start of 791 all-zero\n")
                            else:
                                if ts_790_791_START_matched and ts_791_end > 0 and ts_790_end > 0 and abs(ts_791_end - ts_790_end) <= MAX_END_INTERVAL_BETWEEN_790_791:
                                    print(lineno() + "found 790/791 common end, ONE loop END!!!!!!!!!!!!!!!!!  ts_790: [" + str(ts_790_start) + ", " + str(ts_790_end) + "]  ts_791: [" + str(ts_791_start) + ", " + str(ts_791_end) + "]\n")
                                    CNT_allzero += 1
                                    duration = (ts_790_end + ts_791_end) / 2 - (ts_790_start + ts_791_start) / 2
                                    ts_790_all0_found = False
                                    ts_790_start = -1
                                    ts_790_end = -1
                                    ts_791_all0_found = False
                                    ts_791_start = -1
                                    ts_791_end = -1
                                    ts_790_791_START_matched = False
                                    print("ALL-zero[END]" + str(CNT_allzero) + ", duration: " + str(duration) + "  RESET!!!\n")
                            if range_valid:
                                range_1.append(range_val)
                        elif 2 == aa:
                            diff_timestamp_2 = timestamp_val - last_timestamp_val_2
                            if last_timestamp_val_2 >= 0.0 and 0 == diff_timestamp_2:
                                continue
                            ## print("frame_num_0: " + str(frame_num_0) + ", timestamp_val_0: " + str(timestamp_val_0) + ", last_timestamp_val_0: " + str(last_timestamp_val_0))
                            last_timestamp_val_2 = timestamp_val

                            timestamp_2.append(timestamp_val)
                            if 0 == range_val:
                                cnt_2 = cnt_2 + 1
                                newest_2_range0_ts = timestamp_val
                                if found791allzero(newest_2_range0_ts, newest_3_range0_ts, newest_6_range0_ts, newest_7_range0_ts):
                                    if ts_791_all0_found:
                                        print("791 has already been found, possible this is the END flag of 791!\n")
                                        if ts_790_791_START_matched:
                                            ts_791_end = newest_2_range0_ts
                                            print("790/791 has the same start, check the common end of them now....\n")
                                        else:
                                            print("Still need to search the common start of 790/791!\n")
                                            ts_791_start = newest_2_range0_ts
                                            if ts_790_all0_found:
                                                print("790 all-zero already Found!\n")
                                                if abs(ts_791_start - ts_790_start) <= MAX_INTERVAL_BETWEEN_790_791:
                                                    ts_790_791_START_matched = True
                                                    print(lineno() + "ALL-zero[BEGIN] found!!!!!!\n")
                                                else:
                                                    print("790_allzero doesn't MATCH 791_allzereo in timestamp: " + str(abs(ts_791_start - ts_790_start)) + ", wait for next all0 0f 790 to determine common start!\n")
                                            else:
                                                print(lineno() + "wait start of 790 all-zero to determine common start\n")
                                    else:
                                        ts_791_all0_found = True  ## 全新一次找到790
                                        ts_791_start = newest_2_range0_ts
                                        print("791 all-zero newly Found!\n")

                                        if ts_790_all0_found:
                                            print("790 all-zero already Found!\n")
                                            if abs(ts_791_start - ts_790_start) <= MAX_INTERVAL_BETWEEN_790_791:
                                                ts_790_791_START_matched = True
                                                print("ALL-zero[BEGIN] found!!!!!!\n")
                                            else:
                                                print("790_allzero doesn't MATCH 791_allzereo in timestamp: " + str(abs(ts_791_start - ts_790_start)) + ", wait for next all0 0f 790 to determine common start!\n")
                                        else:
                                            print("wait start of 790 all-zero to determine common start\n")
                            else:
                                if ts_790_791_START_matched and ts_791_end > 0 and ts_790_end > 0 and abs(ts_791_end - ts_790_end) <= MAX_END_INTERVAL_BETWEEN_790_791:
                                    print(lineno() + "found 790/791 common end, ONE loop END!!!!!!!!!!!!!!!!!  ts_790: [" + str(ts_790_start) + ", " + str(ts_790_end) + "]  ts_791: [" + str(ts_791_start) + ", " + str(ts_791_end) + "]\n")
                                    CNT_allzero += 1
                                    duration = (ts_790_end + ts_791_end) / 2 - (ts_790_start + ts_791_start) / 2
                                    ts_790_all0_found = False
                                    ts_790_start = -1
                                    ts_790_end = -1
                                    ts_791_all0_found = False
                                    ts_791_start = -1
                                    ts_791_end = -1
                                    ts_790_791_START_matched = False
                                    print("ALL-zero[END]" + str(CNT_allzero) + ", duration: " + str(duration) + "  RESET!!!\n")
                            if range_valid:
                                range_2.append(range_val)
                        elif 3 == aa:
                            diff_timestamp_3 = timestamp_val - last_timestamp_val_3
                            if last_timestamp_val_3 >= 0.0 and 0 == diff_timestamp_3:
                                continue
                            ## print("frame_num_0: " + str(frame_num_0) + ", timestamp_val_0: " + str(timestamp_val_0) + ", last_timestamp_val_0: " + str(last_timestamp_val_0))
                            last_timestamp_val_3 = timestamp_val

                            timestamp_3.append(timestamp_val)
                            if 0 == range_val:
                                cnt_3 = cnt_3 + 1
                                newest_3_range0_ts = timestamp_val
                                if found791allzero(newest_2_range0_ts, newest_3_range0_ts, newest_6_range0_ts, newest_7_range0_ts):
                                    if ts_791_all0_found:
                                        print("791 has already been found, possible this is the END flag of 791!\n")
                                        if ts_790_791_START_matched:
                                            ts_791_end = newest_2_range0_ts
                                            print("790/791 has the same start, check the common end of them now....\n")
                                        else:
                                            print("Still need to search the common start of 790/791!\n")
                                            ts_791_start = newest_2_range0_ts
                                            if ts_790_all0_found:
                                                print("790 all-zero already Found!\n")
                                                if abs(ts_791_start - ts_790_start) <= MAX_INTERVAL_BETWEEN_790_791:
                                                    ts_790_791_START_matched = True
                                                    print(lineno() + "ALL-zero[BEGIN] found!!!!!!\n")
                                                else:
                                                    print("790_allzero doesn't MATCH 791_allzereo in timestamp: " + str(abs(ts_791_start - ts_790_start)) + ", wait for next all0 0f 790 to determine common start!\n")
                                            else:
                                                print(lineno() + "wait start of 790 all-zero to determine common start\n")
                                    else:
                                        ts_791_all0_found = True  ## 全新一次找到790
                                        ts_791_start = newest_2_range0_ts
                                        print("791 all-zero newly Found!\n")

                                        if ts_790_all0_found:
                                            print("790 all-zero already Found!\n")
                                            if abs(ts_791_start - ts_790_start) <= MAX_INTERVAL_BETWEEN_790_791:
                                                ts_790_791_START_matched = True
                                                print("ALL-zero[BEGIN] found!!!!!!\n")
                                            else:
                                                print("790_allzero doesn't MATCH 791_allzereo in timestamp: " + str(abs(ts_791_start - ts_790_start)) + ", wait for next all0 0f 790 to determine common start!\n")
                                        else:
                                            print("wait start of 790 all-zero to determine common start\n")
                            else:
                                if ts_790_791_START_matched and ts_791_end > 0 and ts_790_end > 0 and abs(ts_791_end - ts_790_end) <= MAX_END_INTERVAL_BETWEEN_790_791:
                                    print(lineno() + "found 790/791 common end, ONE loop END!!!!!!!!!!!!!!!!!  ts_790: [" + str(ts_790_start) + ", " + str(ts_790_end) + "]  ts_791: [" + str(ts_791_start) + ", " + str(ts_791_end) + "]\n")
                                    CNT_allzero += 1
                                    duration = (ts_790_end + ts_791_end) / 2 - (ts_790_start + ts_791_start) / 2
                                    ts_790_all0_found = False
                                    ts_790_start = -1
                                    ts_790_end = -1
                                    ts_791_all0_found = False
                                    ts_791_start = -1
                                    ts_791_end = -1
                                    ts_790_791_START_matched = False
                                    print("ALL-zero[END]" + str(CNT_allzero) + ", duration: " + str(duration) + "  RESET!!!\n")
                            if range_valid:
                                range_3.append(range_val)
                        elif 4 == aa:
                            diff_timestamp_4 = timestamp_val - last_timestamp_val_4
                            if last_timestamp_val_4 >= 0.0 and 0 == diff_timestamp_4:
                                continue
                            ## print("frame_num_0: " + str(frame_num_0) + ", timestamp_val_0: " + str(timestamp_val_0) + ", last_timestamp_val_0: " + str(last_timestamp_val_0))
                            last_timestamp_val_4 = timestamp_val

                            timestamp_4.append(timestamp_val)
                            if 0 == range_val:
                                cnt_4 = cnt_4 + 1
                                newest_4_range0_ts = timestamp_val
                                if found790allzero(newest_0_range0_ts, newest_1_range0_ts, newest_4_range0_ts, newest_5_range0_ts):
                                    if ts_790_all0_found:
                                        print(lineno() + "790 has already been found, possible this is the END flag of 790!\n")
                                        if ts_790_791_START_matched:
                                            ts_790_end = newest_0_range0_ts
                                            print(lineno() + "790/791 has the same start, check the common end of them now....  ts_790_end: " + str(ts_790_end) + "\n")
                                        else:
                                            print("Still need to search the common start of 790/791!\n")
                                            ts_790_start = newest_0_range0_ts
                                            if ts_791_all0_found:
                                                print("791 all-zero already Found!\n")
                                                if abs(ts_791_start - ts_790_start) <= MAX_INTERVAL_BETWEEN_790_791:
                                                    ts_790_791_START_matched = True
                                                    print(lineno() + "ALL-zero[BEGIN] found!!!!!!\n")
                                                else:
                                                    print("790_allzero doesn't MATCH 791_allzereo in timestamp: " + str(abs(ts_791_start - ts_790_start)) + ", wait for next all0 0f 790 to determine common start!\n")
                                            else:
                                                print(lineno() + "wait start of 790 all-zero to determine common start\n")
                                    else:
                                        ts_790_all0_found = True  ## 全新一次找到790
                                        ts_790_start = newest_0_range0_ts
                                        print("790 all-zero newly Found!\n")

                                        if ts_791_all0_found:
                                            print("791 all-zero already Found!\n")
                                            if abs(ts_791_start - ts_790_start) <= MAX_INTERVAL_BETWEEN_790_791:
                                                ts_790_791_START_matched = True
                                                print("ALL-zero[BEGIN] found!!!!!!\n")
                                            else:
                                                print("790_allzero doesn't MATCH 791_allzereo in timestamp: " + str(abs(ts_791_start - ts_790_start)) + ", wait for next all0 0f 791\n")
                                        else:
                                            print("wait start of 791 all-zero\n")
                            else:
                                if ts_790_791_START_matched and ts_791_end > 0 and ts_790_end > 0 and abs(ts_791_end - ts_790_end) <= MAX_END_INTERVAL_BETWEEN_790_791:
                                    print(lineno() + "found 790/791 common end, ONE loop END!!!!!!!!!!!!!!!!!  ts_790: [" + str(ts_790_start) + ", " + str(ts_790_end) + "]  ts_791: [" + str(ts_791_start) + ", " + str(ts_791_end) + "]\n")
                                    CNT_allzero += 1
                                    duration = (ts_790_end + ts_791_end) / 2 - (ts_790_start + ts_791_start) / 2
                                    ts_790_all0_found = False
                                    ts_790_start = -1
                                    ts_790_end = -1
                                    ts_791_all0_found = False
                                    ts_791_start = -1
                                    ts_791_end = -1
                                    ts_790_791_START_matched = False
                                    print("ALL-zero[END]" + str(CNT_allzero) + ", duration: " + str(duration) + "  RESET!!!\n")
                            if range_valid:
                                range_4.append(range_val)
                        elif 5 == aa:
                            diff_timestamp_5 = timestamp_val - last_timestamp_val_5
                            if last_timestamp_val_5 >= 0.0 and 0 == diff_timestamp_5:
                                continue
                            ## print("frame_num_0: " + str(frame_num_0) + ", timestamp_val_0: " + str(timestamp_val_0) + ", last_timestamp_val_0: " + str(last_timestamp_val_0))
                            last_timestamp_val_5 = timestamp_val

                            timestamp_5.append(timestamp_val)
                            if 0 == range_val:
                                cnt_5 = cnt_5 + 1
                                newest_5_range0_ts = timestamp_val
                                if found790allzero(newest_0_range0_ts, newest_1_range0_ts, newest_4_range0_ts, newest_5_range0_ts):
                                    if ts_790_all0_found:
                                        print(lineno() + "790 has already been found, possible this is the END flag of 790!\n")
                                        if ts_790_791_START_matched:
                                            ts_790_end = newest_0_range0_ts
                                            print(lineno() + "790/791 has the same start, check the common end of them now.... ts_790_end: " + str(ts_790_end) + "\n")
                                        else:
                                            print("Still need to search the common start of 790/791!\n")
                                            ts_790_start = newest_0_range0_ts
                                            if ts_791_all0_found:
                                                print("791 all-zero already Found!\n")
                                                if abs(ts_791_start - ts_790_start) <= MAX_INTERVAL_BETWEEN_790_791:
                                                    ts_790_791_START_matched = True
                                                    print(lineno() + "ALL-zero[BEGIN] found!!!!!!\n")
                                                else:
                                                    print("790_allzero doesn't MATCH 791_allzereo in timestamp: " + str(abs(ts_791_start - ts_790_start)) + ", wait for next all0 0f 790 to determine common start!\n")
                                            else:
                                                print(lineno() + "wait start of 790 all-zero to determine common start\n")
                                    else:
                                        ts_790_all0_found = True  ## 全新一次找到790
                                        ts_790_start = newest_0_range0_ts
                                        print(lineno() + "790 all-zero newly Found by 55!  ts_790_start: " + str(ts_790_start) + "\n")

                                        if ts_791_all0_found:
                                            print("791 all-zero already Found!\n")
                                            if abs(ts_791_start - ts_790_start) <= MAX_INTERVAL_BETWEEN_790_791:
                                                ts_790_791_START_matched = True
                                                print(lineno() + "ALL-zero[BEGIN] found!!!!!!\n")
                                            else:
                                                print("790_allzero doesn't MATCH 791_allzereo in timestamp: " + str(abs(ts_791_start - ts_790_start)) + ", wait for next all0 0f 791\n")
                                        else:
                                            print("wait start of 791 all-zero\n")
                            else:
                                if ts_790_791_START_matched and ts_791_end > 0 and ts_790_end > 0 and abs(ts_791_end - ts_790_end) <= MAX_END_INTERVAL_BETWEEN_790_791:
                                    print(lineno() + "found 790/791 common end, ONE loop END!!!!!!!!!!!!!!!!!  ts_790: [" + str(ts_790_start) + ", " + str(ts_790_end) + "]  ts_791: [" + str(ts_791_start) + ", " + str(ts_791_end) + "]\n")
                                    CNT_allzero += 1
                                    duration = (ts_790_end + ts_791_end) / 2 - (ts_790_start + ts_791_start) / 2
                                    ts_790_all0_found = False
                                    ts_790_start = -1
                                    ts_790_end = -1
                                    ts_791_all0_found = False
                                    ts_791_start = -1
                                    ts_791_end = -1
                                    ts_790_791_START_matched = False
                                    print("ALL-zero[END]" + str(CNT_allzero) + ", duration: " + str(duration) + "  RESET!!!\n")
                            if range_valid:
                                range_5.append(range_val)
                        elif 6 == aa:
                            diff_timestamp_6 = timestamp_val - last_timestamp_val_6
                            if last_timestamp_val_6 >= 0.0 and 0 == diff_timestamp_6:
                                continue
                            ## print("frame_num_0: " + str(frame_num_0) + ", timestamp_val_0: " + str(timestamp_val_0) + ", last_timestamp_val_0: " + str(last_timestamp_val_0))
                            last_timestamp_val_6 = timestamp_val

                            timestamp_6.append(timestamp_val)
                            if 0 == range_val:
                                cnt_6 = cnt_6 + 1
                                newest_6_range0_ts = timestamp_val
                                if found791allzero(newest_2_range0_ts, newest_3_range0_ts, newest_6_range0_ts, newest_7_range0_ts):
                                    if ts_791_all0_found:
                                        print("791 has already been found, possible this is the END flag of 791!\n")
                                        if ts_790_791_START_matched:
                                            ts_791_end = newest_2_range0_ts
                                            print("790/791 has the same start, check the common end of them now....\n")
                                        else:
                                            print("Still need to search the common start of 790/791!\n")
                                            ts_791_start = newest_2_range0_ts
                                            if ts_790_all0_found:
                                                print("790 all-zero already Found!\n")
                                                if abs(ts_791_start - ts_790_start) <= MAX_INTERVAL_BETWEEN_790_791:
                                                    ts_790_791_START_matched = True
                                                    print(lineno() + "ALL-zero[BEGIN] found!!!!!!\n")
                                                else:
                                                    print("790_allzero doesn't MATCH 791_allzereo in timestamp: " + str(abs(ts_791_start - ts_790_start)) + ", wait for next all0 0f 790 to determine common start!\n")
                                            else:
                                                print(lineno() + "wait start of 790 all-zero to determine common start\n")
                                    else:
                                        ts_791_all0_found = True  ## 全新一次找到790
                                        ts_791_start = newest_2_range0_ts
                                        print(lineno() + "791 all-zero newly Found by 66!  ts_791_start: " + str(ts_791_start) + "\n")

                                        if ts_790_all0_found:
                                            print("790 all-zero already Found!\n")
                                            if abs(ts_791_start - ts_790_start) <= MAX_INTERVAL_BETWEEN_790_791:
                                                ts_790_791_START_matched = True
                                                print("ALL-zero[BEGIN] found!!!!!!\n")
                                            else:
                                                print("790_allzero doesn't MATCH 791_allzereo in timestamp: " + str(abs(ts_791_start - ts_790_start)) + ", wait for next all0 0f 790 to determine common start!\n")
                                        else:
                                            print("wait start of 790 all-zero to determine common start\n")
                            else:
                                if ts_790_791_START_matched and ts_791_end > 0 and ts_790_end > 0 and abs(ts_791_end - ts_790_end) <= MAX_END_INTERVAL_BETWEEN_790_791:
                                    print(lineno() + "found 790/791 common end, ONE loop END!!!!!!!!!!!!!!!!!  ts_790: [" + str(ts_790_start) + ", " + str(ts_790_end) + "]  ts_791: [" + str(ts_791_start) + ", " + str(ts_791_end) + "]\n")
                                    CNT_allzero += 1
                                    duration = (ts_790_end + ts_791_end) / 2 - (ts_790_start + ts_791_start) / 2
                                    ts_790_all0_found = False
                                    ts_790_start = -1
                                    ts_790_end = -1
                                    ts_791_all0_found = False
                                    ts_791_start = -1
                                    ts_791_end = -1
                                    ts_790_791_START_matched = False
                                    print("ALL-zero[END]" + str(CNT_allzero) + ", duration: " + str(duration) + "  RESET!!!\n")
                            if range_valid:
                                range_6.append(range_val)
                        elif 7 == aa:
                            diff_timestamp_7 = timestamp_val - last_timestamp_val_7
                            if last_timestamp_val_7 >= 0.0 and 0 == diff_timestamp_7:
                                continue
                            ## print("frame_num_0: " + str(frame_num_0) + ", timestamp_val_0: " + str(timestamp_val_0) + ", last_timestamp_val_0: " + str(last_timestamp_val_0))
                            last_timestamp_val_7 = timestamp_val

                            timestamp_7.append(timestamp_val)
                            if 0 == range_val:
                                cnt_7 = cnt_7 + 1
                                newest_7_range0_ts = timestamp_val
                                if found791allzero(newest_2_range0_ts, newest_3_range0_ts, newest_6_range0_ts, newest_7_range0_ts):
                                    if ts_791_all0_found:
                                        print("791 has already been found, possible this is the END flag of 791!\n")
                                        if ts_790_791_START_matched:
                                            ts_791_end = newest_2_range0_ts
                                            print("790/791 has the same start, check the common end of them now....  ts_791_end: " + str(ts_791_end) + "\n")
                                        else:
                                            print("Still need to search the common start of 790/791!\n")
                                            ts_791_start = newest_2_range0_ts
                                            if ts_790_all0_found:
                                                print("790 all-zero already Found!\n")
                                                if abs(ts_791_start - ts_790_start) <= MAX_INTERVAL_BETWEEN_790_791:
                                                    ts_790_791_START_matched = True
                                                    print(lineno() + "ALL-zero[BEGIN] found!!!!!!\n")
                                                else:
                                                    print("790_allzero doesn't MATCH 791_allzereo in timestamp: " + str(abs(ts_791_start - ts_790_start)) + ", wait for next all0 0f 790 to determine common start!\n")
                                            else:
                                                print(lineno() + "wait start of 790 all-zero to determine common start\n")
                                    else:
                                        ts_791_all0_found = True  ## 全新一次找到791
                                        ts_791_start = newest_2_range0_ts
                                        print(lineno() + "791 all-zero newly Found by 77!  ts_791_start: " + str(ts_791_start) + "\n")

                                        if ts_790_all0_found:
                                            print("790 all-zero already Found!\n")
                                            if abs(ts_791_start - ts_790_start) <= MAX_INTERVAL_BETWEEN_790_791:
                                                ts_790_791_START_matched = True
                                                print(lineno() + "ALL-zero[BEGIN] found!!!!!!\n")
                                            else:
                                                print("790_allzero doesn't MATCH 791_allzereo in timestamp: " + str(abs(ts_791_start - ts_790_start)) + ", wait for next all0 0f 790 to determine common start!\n")
                                        else:
                                            print(lineno() + "wait start of 790 all-zero to determine common start\n")
                            else:
                                if ts_790_791_START_matched and ts_791_end > 0 and ts_790_end > 0 and abs(ts_791_end - ts_790_end) <= MAX_END_INTERVAL_BETWEEN_790_791:
                                    print(lineno() + "found 790/791 common end, ONE loop END!!!!!!!!!!!!!!!!!  ts_790: [" + str(ts_790_start) + ", " + str(ts_790_end) + "]  ts_791: [" + str(ts_791_start) + ", " + str(ts_791_end) + "]\n")
                                    CNT_allzero += 1
                                    duration = (ts_790_end + ts_791_end) / 2 - (ts_790_start + ts_791_start) / 2
                                    ts_790_all0_found = False
                                    ts_790_start = -1
                                    ts_790_end = -1
                                    ts_791_all0_found = False
                                    ts_791_start = -1
                                    ts_791_end = -1
                                    ts_790_791_START_matched = False
                                    print("ALL-zero[END]" + str(CNT_allzero) + ", duration: " + str(duration) + "  RESET!!!\n")
                            if range_valid:
                                range_7.append(range_val)

    return range_0, timestamp_0, cnt_0, range_1, timestamp_1, cnt_1, range_2, timestamp_2, cnt_2, range_3, timestamp_3, cnt_3, range_4, timestamp_4, cnt_4, range_5, timestamp_5, cnt_5, range_6, timestamp_6, cnt_6, range_7, timestamp_7, cnt_7

if __name__ == "__main__":
    if len(sys.argv) == 2:
        # frame_NO_0, range_0, timestamp_0, range_start_0, timestamp_start_0, range_end_0, timestamp_end_0, frame_NO_1, range_valid_1, timestamp_1, range_start_1, timestamp_start_1, range_end_1, timestamp_end_1 = loadradar(sys.argv[1])
        #  frame_NO_0, range_0, timestamp_0 = loadradar(sys.argv[1])
        range_0, ts_0, cnt_0, range_1, ts_1, cnt_1, range_2, ts_2, cnt_2, range_3, ts_3, cnt_3, range_4, ts_4, cnt_4, range_5, ts_5, cnt_5, range_6, ts_6, cnt_6, range_7, ts_7, cnt_7  = loadradar(sys.argv[1])
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
        figure2 = plt.figure("Sonar Range")
        figure2.suptitle('Sonar Range Curve', x=0.50, y=0.96, fontsize=24)
        font = {'family': 'serif',
                'color':  'blue',
                'weight': 'normal',
                'size': 16,
               }
        ax_range_0 = figure2.add_subplot(4, 2, 1)
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
        ax_range_1 = figure2.add_subplot(4, 2, 2)
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
        ax_range_2 = figure2.add_subplot(4, 2, 3)
        ax_range_2.plot(range_2, '-r')
        curves = ["sonar2"]
        ax_range_2.legend(curves, prop={'size':18})
        leg = ax_range_2.get_legend()
        leg.legendHandles[0].set_color('blue')
        if 0 == len(range_2):
            ax_range_2.text(0.5, 0.5, 'range is empty', horizontalalignment='center', verticalalignment='center', transform=ax_range_2.transAxes, fontdict=font)
        else:
            ax_range_2.text(0.5, 0.5, "CNT: " + str(len(range_2)) + "  CNT_0: " + str(cnt_2) + "\nmin: " + "{0:.1f}".format(np.min(range_2)) + "    mean: " + "{0:.1f}".format(np.mean(range_2)) + "    max: " + "{0:.1f}".format(np.max(range_2)), horizontalalignment='center', verticalalignment='center', transform=ax_range_2.transAxes, fontdict=font)
        ax_range_2.grid(True)
        ax_range_3 = figure2.add_subplot(4, 2, 4)
        ax_range_3.plot(range_3, '-r')
        curves = ["sonar3"]
        ax_range_3.legend(curves, prop={'size':18})
        leg = ax_range_3.get_legend()
        leg.legendHandles[0].set_color('blue')
        if 0 == len(range_3):
            ax_range_3.text(0.5, 0.5, 'range is empty', horizontalalignment='center', verticalalignment='center', transform=ax_range_3.transAxes, fontdict=font)
        else:
            ax_range_3.text(0.5, 0.5, "CNT: " + str(len(range_3)) + "  CNT_0: " + str(cnt_3) + "\nmin: " + "{0:.1f}".format(np.min(range_3)) + "    mean: " + "{0:.1f}".format(np.mean(range_3)) + "    max: " + "{0:.1f}".format(np.max(range_3)), horizontalalignment='center', verticalalignment='center', transform=ax_range_3.transAxes, fontdict=font)
        ax_range_3.grid(True)
        ax_range_4 = figure2.add_subplot(4, 2, 5)
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
        ax_range_5 = figure2.add_subplot(4, 2, 6)
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
        ax_range_6 = figure2.add_subplot(4, 2, 7)
        ax_range_6.plot(range_6, '-r')
        curves = ["sonar6"]
        ax_range_6.legend(curves, prop={'size':18})
        leg = ax_range_6.get_legend()
        leg.legendHandles[0].set_color('blue')
        if 0 == len(range_6):
            ax_range_6.text(0.5, 0.5, 'range is empty', horizontalalignment='center', verticalalignment='center', transform=ax_range_6.transAxes, fontdict=font)
        else:
            ax_range_6.text(0.5, 0.5, "CNT: " + str(len(range_6)) + "  CNT_0: " + str(cnt_6) + "\nmin: " + "{0:.1f}".format(np.min(range_6)) + "    mean: " + "{0:.1f}".format(np.mean(range_6)) + "    max: " + "{0:.1f}".format(np.max(range_6)), horizontalalignment='center', verticalalignment='center', transform=ax_range_6.transAxes, fontdict=font)
        ax_range_6.grid(True)
        ax_range_7 = figure2.add_subplot(4, 2, 8)
        ax_range_7.plot(range_7, '-r')
        curves = ["sonar7"]
        ax_range_7.legend(curves, prop={'size':18})
        leg = ax_range_7.get_legend()
        leg.legendHandles[0].set_color('blue')
        if 0 == len(range_7):
            ax_range_7.text(0.5, 0.5, 'range is empty', horizontalalignment='center', verticalalignment='center', transform=ax_range_7.transAxes, fontdict=font)
        else:
            ax_range_7.text(0.5, 0.5, "CNT: " + str(len(range_7)) + "  CNT_0: " + str(cnt_7) + "\nmin: " + "{0:.1f}".format(np.min(range_7)) + "    mean: " + "{0:.1f}".format(np.mean(range_7)) + "    max: " + "{0:.1f}".format(np.max(range_7)), horizontalalignment='center', verticalalignment='center', transform=ax_range_7.transAxes, fontdict=font)
        ax_range_7.grid(True)
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
