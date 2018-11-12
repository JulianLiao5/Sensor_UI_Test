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
  dist_x = []
  distance = []
  velocity = []
  angle = []
  power = []
  with open(filename) as myfile:
    for line in myfile:
            dist_x_name, dist_x_var = line.partition("distance_x: ")[::2]
            dist_x_item = dist_x_var.split(" ")[0]
            dist_x.append(float(dist_x_item))
            name, var = line.partition("distance: ")[::2]
            dist_item = var.split(" ")[0]
            distance.append(float(dist_item))
            name, var = line.partition("RadialVelocity: ")[::2]
            velocity_item = var.split(" ")[0]
            velocity.append(float(velocity_item))
            name, var = line.partition("Angle: ")[::2]
            angle_item = var.split(" ")[0]
            angle.append(float(angle_item))
            name, var = line.partition("Power: ")[::2]
            power_item = var.split(" ")[0]
            power.append(float(power_item))
    CNT = 0
    return dist_x, distance, velocity, angle, power

if __name__ == "__main__":
    if len(sys.argv) == 2:
        dist_x, distance, velocity, angle, power = loadradar(sys.argv[1])
        fig = plt.figure("dist_x")
        plt.plot(dist_x)
        plt.ylabel('dist_x')
        # plt.yticks(np.arange(int(np.min(distance)), int(np.max(distance)) + 1, 1))
        font = {'family': 'serif',
        'color':  'darkorchid',
        'weight': 'normal',
        'size': 14,
        }
        if False:
            plt.text(10, 15, "min: " + str(np.min(dist_x)) + ", mean: " +
                 "{0:.4f}".format(np.mean(dist_x)) + ", max: " + str(np.max(dist_x)), fontdict=font)
        else:
            plt.text(9500, 5.10, "Ground truth: suppose 5.24m\n    min: " + str(np.min(dist_x)) + ", mean: " +
                 "{0:.4f}".format(np.mean(dist_x)) + ", max: " + str(np.max(dist_x)) + ", std dev: " + "{0:.4f}".format(np.std(dist_x)) +
                 "\n    error: " + "{:.4%}".format((np.mean(dist_x) - 5.24) / 5.24), fontdict=font)
        plt.grid(True)
        fig = plt.figure("radar range")
        plt.plot(distance)
        plt.ylabel('distance')
        plt.yticks(np.arange(int(np.min(distance)), int(np.max(distance)) + 1, 1))
        font = {'family': 'serif',
        'color':  'darkorchid',
        'weight': 'normal',
        'size': 14,
        }
        if False:
            plt.text(10, 15, "min: " + str(np.min(distance)) + ", mean: " +
                 "{0:.4f}".format(np.mean(distance)) + ", max: " + str(np.max(distance)), fontdict=font)
        else:
            plt.text(9500, 5.10, "Ground truth: suppose 5.24m\n    min: " + str(np.min(distance)) + ", mean: " +
                 "{0:.4f}".format(np.mean(distance)) + ", max: " + str(np.max(distance)) + ", std dev: " + "{0:.4f}".format(np.std(distance)) +
                 "\n    error: " + "{:.4%}".format((np.mean(distance) - 5.24) / 5.24), fontdict=font)
        plt.grid(True)
        fig = plt.figure("velocity")
        plt.plot(velocity)
        plt.ylabel('velocity')
        # plt.yticks(np.arange(np.min(velocity), np.max(velocity)))
        font = {'family': 'serif',
        'color':  'darkred',
        'weight': 'normal',
        'size': 14,
        }
        if True:
            if True:
                plt.text(20, -0.1, "min: " + str(np.min(velocity)) + ", mean: " + "{0:.4f}".format(np.mean(velocity)) +
                     ", max: " + str(np.max(velocity)), fontdict=font)
            else:
                plt.text(250, -0.9, "Ground truth: 0.0, min: " + str(np.min(velocity)) + ", mean: " + "{0:.4f}".format(np.mean(velocity)) +
                     ", max: " + str(np.max(velocity)) + ", std dev: " + "{0:.4f}".format(np.std(velocity)), fontdict=font)
        else:
            plt.text(200, 1, "Ground truth: 0.0, min: " + str(np.min(velocity)) + ", mean: " + "{0:.4f}".format(np.mean(velocity)) +
                 ", max: " + str(np.max(velocity)) + ", std dev: " + "{0:.4f}".format(np.std(velocity)) +
                 "\n    error: " + "{:.4%}".format((np.mean(velocity) - 5.0) / 5.0), fontdict=font)
        plt.grid(True)
        fig = plt.figure("angle")
        plt.plot(angle)
        plt.ylabel('angle')
        plt.yticks(np.arange(int(np.min(angle)), round(np.max(angle)) + 1, 1))
        font = {'family': 'serif',
            'color':  'darkorange',
            'weight': 'normal',
            'size': 14,
            }
        if True:
            if True:
                plt.text(50, -4.7, "Ground truth: 0.0deg\n    min: " + str(np.min(angle)) + ", mean: "
                     + "{0:.4f}".format(np.mean(angle)) + ", max: " + str(np.max(angle))  + ", std dev: " + "{0:.4f}".format(np.std(angle))
                     , fontdict=font)
            else:
                plt.text(20, 15, "min: " + str(np.min(angle)) + ", mean: "
                     + "{0:.4f}".format(np.mean(angle)) + ", max: " + str(np.max(angle)), fontdict=font)
        else:
            plt.text(50, -4, "Ground truth: 0.0deg\n    min: " + str(np.min(angle)) + ", mean: "
                 + "{0:.4f}".format(np.mean(angle)) + ", max: " + str(np.max(angle))  + ", std dev: " + "{0:.4f}".format(np.std(angle))
                 + "\n    error: " + "{:.4%}".format((np.mean(angle) - (-20.0)) / (-20.0)),
                fontdict=font)
        plt.grid(True)
        fig = plt.figure("power")
        plt.plot(power)
        plt.ylabel('power')
        font = {'family': 'serif',
            'color':  'darkorange',
            'weight': 'normal',
            'size': 14,
            }
        plt.text(6000, -30.0, "min: " + str(np.min(power)) + ", mean: " + "{0:.4f}".format(np.mean(power)) + ", max: " + str(np.max(power)),
            fontdict=font)
        plt.grid(True)
        plt.show()
    else:
        print("Usage: " + sys.argv[0] + " radar.txt")
