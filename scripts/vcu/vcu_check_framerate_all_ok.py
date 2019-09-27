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

def loadvcu(filename):
    timestamp_161 = []
    timestamp_151 = []
    timestamp_141 = []
    timestamp_131 = []
    timestamp_121 = []
    timestamp_111 = []
    timestamp_171 = []
    ts_radar_0 = []
    ts_radar_1 = []
    ts_radar_2 = []
    ts_radar_3 = []
    ts_radar_4 = []
    ts_radar_5 = []
    ts_sonar_0 = []
    ts_sonar_1 = []
    vcu_IDs = [161, 151, 141, 131, 121, 111, 171]
    radar_IDs = [0, 1, 2, 3, 4, 5, 6, 7]
    sonar_IDs = [0, 1]
    IDs = [0, 1, 2, 3, 4, 5, 6, 7, 161, 151, 141, 131, 121, 111, 171]
    with open(filename) as myfile:
            for line in myfile:
                line = line[:-1]    # deletes extra line
                for aa in IDs:
                  if re.search("liaomeng vcu" + str(aa) + " ", line, re.IGNORECASE):
                    name, var = line.partition("liaomeng vcu" + str(aa) + " ")[::2]
                    interval = var.split(" ")[0]
                    interval = float(interval)

                    if 161 == aa:
                        timestamp_161.append(interval)
                    elif 151 == aa:
                        timestamp_151.append(interval)
                    elif 141 == aa:
                        timestamp_141.append(interval)
                    elif 131 == aa:
                        timestamp_131.append(interval)
                    elif 121 == aa:
                        timestamp_121.append(interval)
                    elif 111 == aa:
                        timestamp_111.append(interval)
                    elif 171 == aa:
                        timestamp_171.append(interval)
                  elif re.search("liaomeng radar" + str(aa) + " ", line, re.IGNORECASE):
                    name, var = line.partition("liaomeng radar" + str(aa) + " ")[::2]
                    interval = var.split(" ")[0]
                    interval = float(interval)

                    if 0 == aa:
                        ts_radar_0.append(interval)
                    elif 1 == aa:
                        ts_radar_1.append(interval)
                    elif 2 == aa:
                        ts_radar_2.append(interval)
                    elif 3 == aa:
                        ts_radar_3.append(interval)
                    elif 4 == aa:
                        ts_radar_4.append(interval)
                    elif 5 == aa:
                        ts_radar_5.append(interval)
                  elif re.search("liaomeng sonar" + str(aa) + " ", line, re.IGNORECASE):
                    name, var = line.partition("liaomeng sonar" + str(aa) + " ")[::2]
                    interval = var.split(" ")[0]
                    interval = float(interval)

                    if 0 == aa:
                        ts_sonar_0.append(interval)
                    elif 1 == aa:
                        ts_sonar_1.append(interval)

    return timestamp_161, timestamp_151, timestamp_141, timestamp_131, timestamp_121, timestamp_111, timestamp_171, ts_radar_0, ts_radar_1, ts_radar_2, ts_radar_3, ts_radar_4, ts_radar_5, ts_sonar_0, ts_sonar_1

if __name__ == "__main__":
    if len(sys.argv) == 2:
        timestamp_161, timestamp_151, timestamp_141, timestamp_131, timestamp_121, timestamp_111, timestamp_171, ts_radar_0, ts_radar_1, ts_radar_2, ts_radar_3, ts_radar_4, ts_radar_5, ts_sonar_0, ts_sonar_1 = loadvcu(sys.argv[1])
        figure1 = plt.figure("VCU diff time")
        figure1.suptitle('VCU diff_time', x=0.50, y=0.96, fontsize=24)
        ax_1 = figure1.add_subplot(4, 2, 1)
        ax_1.plot(timestamp_161, '-b')
        font = {'family': 'serif',
                #'color':  'blue',
                'color':  'black',
                'weight': 'normal',
                'size': 16,
               }
        ax_1.text(50, 15, "161 interval:    mean: " + "{0:.2f}".format(np.mean(timestamp_161)) + "ms    max: " + "{0:.2f}".format(np.max(timestamp_161)) + "ms", fontdict=font)
        #ax_1.set_ylabel('ID0 diff timestamp[milliseconds]', size=10)
        ax_1.grid(True)
        curves = ["VCU  -  161"]
        ax_1.legend(curves, prop={'size':18})
        leg = ax_1.get_legend()
        leg.legendHandles[0].set_color('blue')
        ax_2 = figure1.add_subplot(4, 2, 2)
        ax_2.plot(timestamp_151, '-g')
        font = {'family': 'serif',
                #'color':  'green',
                'color':  'black',
                'weight': 'normal',
                'size': 16,
               }
        ax_2.text(50, 15, "151 interval:    mean: " + "{0:.2f}".format(np.mean(timestamp_151)) + "ms    max: " + "{0:.2f}".format(np.max(timestamp_151)) + "ms", fontdict=font)
        #ax_2.set_ylabel('ID1 diff timestamp[milliseconds]', size=10)
        ax_2.grid(True)
        curves = ["VCU  -  151"]
        ax_2.legend(curves, prop={'size':18})
        leg = ax_2.get_legend()
        leg.legendHandles[0].set_color('green')
        ax_3 = figure1.add_subplot(4, 2, 3)
        ax_3.plot(timestamp_141, '-r')
        ax_3.text(50, 15, "141 interval:    mean: " + "{0:.2f}".format(np.mean(timestamp_141)) + "ms    max: " + "{0:.2f}".format(np.max(timestamp_141)) + "ms", fontdict=font)
        ax_3.grid(True)
        curves = ["VCU  -  141"]
        ax_3.legend(curves, prop={'size':18})
        leg = ax_3.get_legend()
        leg.legendHandles[0].set_color('blue')
        ax_4 = figure1.add_subplot(4, 2, 4)
        ax_4.plot(timestamp_131, '-r')
        ax_4.text(50, 15, "131 interval:    mean: " + "{0:.2f}".format(np.mean(timestamp_131)) + "ms    max: " + "{0:.2f}".format(np.max(timestamp_131)) + "ms", fontdict=font)
        ax_4.grid(True)
        curves = ["VCU  -  131"]
        ax_4.legend(curves, prop={'size':18})
        leg = ax_4.get_legend()
        leg.legendHandles[0].set_color('blue')
        ax_5 = figure1.add_subplot(4, 2, 5)
        ax_5.plot(timestamp_121, '-r')
        ax_5.text(50, 15, "121 interval:    mean: " + "{0:.2f}".format(np.mean(timestamp_121)) + "ms    max: " + "{0:.2f}".format(np.max(timestamp_121)) + "ms", fontdict=font)
        ax_5.grid(True)
        curves = ["VCU  -  121"]
        ax_5.legend(curves, prop={'size':18})
        leg = ax_5.get_legend()
        leg.legendHandles[0].set_color('blue')
        ax_6 = figure1.add_subplot(4, 2, 6)
        ax_6.plot(timestamp_111, '-r')
        ax_6.text(50, 15, "111 interval:    mean: " + "{0:.2f}".format(np.mean(timestamp_111)) + "ms    max: " + "{0:.2f}".format(np.max(timestamp_111)) + "ms", fontdict=font)
        ax_6.grid(True)
        curves = ["VCU  -  111"]
        ax_6.legend(curves, prop={'size':18})
        leg = ax_6.get_legend()
        leg.legendHandles[0].set_color('blue')
        ax_7 = figure1.add_subplot(4, 2, 7)
        ax_7.plot(timestamp_171, '-r')
        ax_7.text(50, 15, "171 interval:    mean: " + "{0:.2f}".format(np.mean(timestamp_171)) + "ms    max: " + "{0:.2f}".format(np.max(timestamp_171)) + "ms", fontdict=font)
        ax_7.grid(True)
        curves = ["VCU  -  171"]
        ax_7.legend(curves, prop={'size':18})
        leg = ax_7.get_legend()
        leg.legendHandles[0].set_color('magenta')

        figure2 = plt.figure("RADAR diff time")
        figure2.suptitle('RADAR diff_time', x=0.50, y=0.96, fontsize=24)
        ax_radar_1 = figure2.add_subplot(3, 2, 1)
        ax_radar_1.plot(ts_radar_0, '-b')
        font = {'family': 'serif',
                #'color':  'blue',
                'color':  'black',
                'weight': 'normal',
                'size': 16,
               }
        ax_radar_1.text(50, 30, "ID0 interval:    mean: " + "{0:.2f}".format(np.mean(ts_radar_0)) + "ms    max: " + "{0:.2f}".format(np.max(ts_radar_0)) + "ms", fontdict=font)
        #ax_1.set_ylabel('ID0 diff timestamp[milliseconds]', size=10)
        ax_radar_1.grid(True)
        curves = ["RADAR  -  ID0"]
        ax_radar_1.legend(curves, prop={'size':18})
        leg = ax_radar_1.get_legend()
        leg.legendHandles[0].set_color('blue')
        ax_radar_2 = figure2.add_subplot(3, 2, 2)
        ax_radar_2.plot(ts_radar_1, '-g')
        ax_radar_2.text(50, 30, "ID1 interval:    mean: " + "{0:.2f}".format(np.mean(ts_radar_1)) + "ms    max: " + "{0:.2f}".format(np.max(ts_radar_1)) + "ms", fontdict=font)
        font = {'family': 'serif',
                #'color':  'green',
                'color':  'black',
                'weight': 'normal',
                'size': 16,
               }
        #ax_2.set_ylabel('ID1 diff timestamp[milliseconds]', size=10)
        ax_radar_2.grid(True)
        curves = ["RADAR  -  ID1"]
        ax_radar_2.legend(curves, prop={'size':18})
        leg = ax_radar_2.get_legend()
        leg.legendHandles[0].set_color('green')
        ax_radar_3 = figure2.add_subplot(3, 2, 3)
        ax_radar_3.plot(ts_radar_2, '-r')
        ax_radar_3.text(50, 30, "ID2 interval:    mean: " + "{0:.2f}".format(np.mean(ts_radar_2)) + "ms    max: " + "{0:.2f}".format(np.max(ts_radar_2)) + "ms", fontdict=font)
        ax_radar_3.grid(True)
        curves = ["RADAR  -  ID2"]
        ax_radar_3.legend(curves, prop={'size':18})
        leg = ax_radar_3.get_legend()
        leg.legendHandles[0].set_color('blue')
        ax_radar_4 = figure2.add_subplot(3, 2, 4)
        ax_radar_4.plot(ts_radar_3, '-r')
        ax_radar_4.text(50, 30, "ID3 interval:    mean: " + "{0:.2f}".format(np.mean(ts_radar_3)) + "ms    max: " + "{0:.2f}".format(np.max(ts_radar_3)) + "ms", fontdict=font)
        ax_radar_4.grid(True)
        curves = ["RADAR  -  ID3"]
        ax_radar_4.legend(curves, prop={'size':18})
        leg = ax_radar_4.get_legend()
        leg.legendHandles[0].set_color('blue')
        ax_radar_5 = figure2.add_subplot(3, 2, 5)
        ax_radar_5.plot(ts_radar_4, '-r')
        ax_radar_5.text(50, 30, "ID4 interval:    mean: " + "{0:.2f}".format(np.mean(ts_radar_4)) + "ms    max: " + "{0:.2f}".format(np.max(ts_radar_4)) + "ms", fontdict=font)
        ax_radar_5.grid(True)
        curves = ["RADAR  -  ID4"]
        ax_radar_5.legend(curves, prop={'size':18})
        leg = ax_radar_5.get_legend()
        leg.legendHandles[0].set_color('blue')
        ax_radar_6 = figure2.add_subplot(3, 2, 6)
        ax_radar_6.plot(ts_radar_5, '-r')
        ax_radar_6.text(50, 30, "ID5 interval:    mean: " + "{0:.2f}".format(np.mean(ts_radar_5)) + "ms    max: " + "{0:.2f}".format(np.max(ts_radar_5)) + "ms", fontdict=font)
        ax_radar_6.grid(True)
        curves = ["RADAR  -  ID5"]
        ax_radar_6.legend(curves, prop={'size':18})
        leg = ax_radar_6.get_legend()
        leg.legendHandles[0].set_color('blue')

        figure3 = plt.figure("SONAR diff time")
        figure3.suptitle('SONAR diff_time', x=0.50, y=0.96, fontsize=24)
        ax_sonar_1 = figure3.add_subplot(2, 1, 1)
        ax_sonar_1.plot(ts_sonar_0, '-b')
        font = {'family': 'serif',
                #'color':  'blue',
                'color':  'black',
                'weight': 'normal',
                'size': 16,
               }
        ax_sonar_1.text(50, 20, "ID0 interval:    mean: " + "{0:.2f}".format(np.mean(ts_sonar_0)) + "ms    max: " + "{0:.2f}".format(np.max(ts_sonar_0)) + "ms", fontdict=font)
        #ax_1.set_ylabel('ID0 diff timestamp[milliseconds]', size=10)
        ax_sonar_1.grid(True)
        curves = ["SONAR  -  ID0"]
        ax_sonar_1.legend(curves, prop={'size':18})
        leg = ax_sonar_1.get_legend()
        leg.legendHandles[0].set_color('blue')
        ax_sonar_2 = figure3.add_subplot(2, 1, 2)
        ax_sonar_2.plot(ts_sonar_1, '-g')
        font = {'family': 'serif',
                #'color':  'green',
                'color':  'black',
                'weight': 'normal',
                'size': 16,
               }
        ax_sonar_2.text(50, 20, "ID1 interval:    mean: " + "{0:.2f}".format(np.mean(ts_sonar_1)) + "ms    max: " + "{0:.2f}".format(np.max(ts_sonar_1)) + "ms", fontdict=font)
        #ax_2.set_ylabel('ID1 diff timestamp[milliseconds]', size=10)
        ax_sonar_2.grid(True)
        curves = ["SONAR  -  ID1"]
        ax_sonar_2.legend(curves, prop={'size':18})
        leg = ax_sonar_2.get_legend()
        leg.legendHandles[0].set_color('green')

        plt.show()
    else:
        print("Usage: " + sys.argv[0] + " radar.txt")
