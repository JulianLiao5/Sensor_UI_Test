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
    m = np.loadtxt(filename, delimiter=",")
    timestamp_161 = [vec[0] for vec in m if vec[1] == 353]
    timestamp_151 = [vec[0] for vec in m if vec[1] == 337]
    timestamp_141 = [vec[0] for vec in m if vec[1] == 321]
    timestamp_131 = [vec[0] for vec in m if vec[1] == 305]
    timestamp_121 = [vec[0] for vec in m if vec[1] == 289]
    timestamp_111 = [vec[0] for vec in m if vec[1] == 273]
    timestamp_171 = [vec[0] for vec in m if vec[1] == 369]
    ts_790 = [vec[0] for vec in m if vec[1] == 1936]
    ts_791 = [vec[0] for vec in m if vec[1] == 1937]
    diff_161 = np.diff(timestamp_161)
    diff_151 = np.diff(timestamp_151)
    diff_141 = np.diff(timestamp_141)
    diff_131 = np.diff(timestamp_131)
    diff_121 = np.diff(timestamp_121)
    diff_111 = np.diff(timestamp_111)
    diff_171 = np.diff(timestamp_171)
    diff_161 = [item for item in diff_161 if (item != 0)]
    diff_151 = [item for item in diff_151 if (item != 0)]
    diff_141 = [item for item in diff_141 if (item != 0)]
    diff_131 = [item for item in diff_131 if (item != 0)]
    diff_121 = [item for item in diff_121 if (item != 0)]
    diff_111 = [item for item in diff_111 if (item != 0)]
    diff_171 = [item for item in diff_171 if (item != 0)]
    diff_790 = np.diff(ts_790)
    diff_791 = np.diff(ts_791)
    diff_790 = [item for item in diff_790 if (item != 0)]
    diff_791 = [item for item in diff_791 if (item != 0)]

    return diff_161, diff_151, diff_141, diff_131, diff_121, diff_111, diff_171, diff_790, diff_791

if __name__ == "__main__":
    if len(sys.argv) == 2:
        diff_161, diff_151, diff_141, diff_131, diff_121, diff_111, diff_171, diff_790, diff_791 = loadvcu(sys.argv[1])
        figure1 = plt.figure("vcu framerate")
        figure1.suptitle('vcu framerate\n  unit: ms', x=0.50, y=0.98, fontsize=24)
        ax_1 = figure1.add_subplot(4, 2, 1)
        ax_1.plot(diff_161, '-b')
        font = {'family': 'serif',
                #'color':  'blue',
                'color':  'black',
                'weight': 'normal',
                'size': 16,
               }
        curves = ["VCU - 161"]
        ax_1.legend(curves, prop={'size':18})
        leg = ax_1.get_legend()
        leg.legendHandles[0].set_color('green')
        ax_1.text(0, 21, "vcu_161 period:  mean: " + "{0:.2f}".format(np.mean(diff_161)) + "  max: " + "{0:.2f}".format(np.max(diff_161)), fontdict=font)
        #ax_1.set_ylabel('ID0 diff timestamp[milliseconds]', size=10)
        ax_1.grid(True)
        ax_2 = figure1.add_subplot(4, 2, 2)
        ax_2.plot(diff_151, '-g')
        font = {'family': 'serif',
                #'color':  'green',
                'color':  'black',
                'weight': 'normal',
                'size': 16,
               }
        ax_2.text(0, 21, "vcu_151 period:  mean: " + "{0:.2f}".format(np.mean(diff_151)) + "  max: " + "{0:.2f}".format(np.max(diff_151)), fontdict=font)
        #ax_2.set_ylabel('ID1 diff timestamp[milliseconds]', size=10)
        curves = ["VCU - 151"]
        ax_2.legend(curves, prop={'size':18})
        leg = ax_2.get_legend()
        leg.legendHandles[0].set_color('green')
        ax_2.grid(True)
        ax_3 = figure1.add_subplot(4, 2, 3)
        ax_3.plot(diff_141, '-r')
        font = {'family': 'serif',
                #'color':  'green',
                'color':  'black',
                'weight': 'normal',
                'size': 16,
               }
        ax_3.text(0, 21, "vcu_141 period:  mean: " + "{0:.2f}".format(np.mean(diff_141)) + "  max: " + "{0:.2f}".format(np.max(diff_141)), fontdict=font)
        #ax_2.set_ylabel('ID1 diff timestamp[milliseconds]', size=10)
        curves = ["VCU - 141"]
        ax_3.legend(curves, prop={'size':18})
        leg = ax_3.get_legend()
        leg.legendHandles[0].set_color('green')
        ax_3.grid(True)
        ax_4 = figure1.add_subplot(4, 2, 4)
        ax_4.plot(diff_131, '-m')
        font = {'family': 'serif',
                #'color':  'green',
                'color':  'black',
                'weight': 'normal',
                'size': 16,
               }
        ax_4.text(0, 21, "vcu_131 period:  mean: " + "{0:.2f}".format(np.mean(diff_131)) + "  max: " + "{0:.2f}".format(np.max(diff_131)), fontdict=font)
        #ax_2.set_ylabel('ID1 diff timestamp[milliseconds]', size=10)
        curves = ["VCU - 131"]
        ax_4.legend(curves, prop={'size':18})
        leg = ax_4.get_legend()
        leg.legendHandles[0].set_color('green')
        ax_4.grid(True)
        ax_5 = figure1.add_subplot(4, 2, 5)
        ax_5.plot(diff_121, '-r')
        font = {'family': 'serif',
                #'color':  'green',
                'color':  'black',
                'weight': 'normal',
                'size': 16,
               }
        ax_5.text(0, 21, "vcu_121 period:  mean: " + "{0:.2f}".format(np.mean(diff_121)) + "  max: " + "{0:.2f}".format(np.max(diff_121)), fontdict=font)
        #ax_2.set_ylabel('ID1 diff timestamp[milliseconds]', size=10)
        curves = ["VCU - 121"]
        ax_5.legend(curves, prop={'size':18})
        leg = ax_5.get_legend()
        leg.legendHandles[0].set_color('green')
        ax_5.grid(True)
        ax_6 = figure1.add_subplot(4, 2, 6)
        ax_6.plot(diff_111, '-m')
        font = {'family': 'serif',
                #'color':  'green',
                'color':  'black',
                'weight': 'normal',
                'size': 16,
               }
        ax_6.text(0, 21, "vcu_111 period:  mean: " + "{0:.2f}".format(np.mean(diff_111)) + "  max: " + "{0:.2f}".format(np.max(diff_111)), fontdict=font)
        #ax_2.set_ylabel('ID1 diff timestamp[milliseconds]', size=10)
        curves = ["VCU - 111"]
        ax_6.legend(curves, prop={'size':18})
        leg = ax_6.get_legend()
        leg.legendHandles[0].set_color('green')
        ax_6.grid(True)
        ax_7 = figure1.add_subplot(4, 2, 7)
        ax_7.plot(diff_171, '-m')
        font = {'family': 'serif',
                #'color':  'green',
                'color':  'black',
                'weight': 'normal',
                'size': 16,
               }
        ax_7.text(0, 21, "vcu_171 period:  mean: " + "{0:.2f}".format(np.mean(diff_171)) + "  max: " + "{0:.2f}".format(np.max(diff_171)), fontdict=font)
        #ax_2.set_ylabel('ID1 diff timestamp[milliseconds]', size=10)
        curves = ["VCU - 171"]
        ax_7.legend(curves, prop={'size':18})
        leg = ax_7.get_legend()
        leg.legendHandles[0].set_color('green')
        ax_7.grid(True)

        plt.show()
    else:
        print("Usage: " + sys.argv[0] + " radar.txt")
