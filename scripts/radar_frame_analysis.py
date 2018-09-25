#!/usr/bin/env python
# coding=utf-8

import matplotlib.pyplot as plt
import numpy as np
import re
import sys

def loadradar(filename):
  distance = []
  velocity = []
  angle = []
  power = []
  with open(filename) as myfile:
    for line in myfile:
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
    return distance, velocity, angle, power

if __name__ == "__main__":
    if len(sys.argv) == 2:
        distance, velocity, angle, power = loadradar("./5m_0deg_ana.txt")
        print("min: " + str(np.min(distance)) + ", mean: " + str(np.mean(distance)) + ", max: " + str(np.max(distance)))
        fig = plt.figure("radar range")
        plt.plot(distance)
        plt.ylabel('distance')
        plt.text(0.5, 0.5, "min: " + str(np.min(distance)) + ", mean: " + "{0:.4f}".format(np.mean(distance)) + ", max: " + str(np.max(distance)),
            horizontalalignment='right', verticalalignment='top', transform=plt.gca().transAxes)
        plt.grid(True)
        fig = plt.figure("velocity")
        plt.plot(velocity)
        plt.ylabel('velocity')
        plt.text(0.5, 0.5, "min: " + str(np.min(velocity)) + ", mean: " + str(np.mean(velocity)) + ", max: " + str(np.max(velocity)),
            horizontalalignment='left', verticalalignment='bottom', transform=plt.gca().transAxes)
        plt.grid(True)
        fig = plt.figure("angle")
        plt.plot(angle)
        plt.ylabel('angle')
        plt.text(0.5, 0.5, "min: " + str(np.min(angle)) + ", mean: " + "{0:.4f}".format(np.mean(angle)) + ", max: " + str(np.max(angle)),
            horizontalalignment='center', verticalalignment='center', transform=plt.gca().transAxes)
        plt.grid(True)
        fig = plt.figure("power")
        plt.plot(power)
        plt.ylabel('power')
        plt.text(0.5, 0.5, "min: " + str(np.min(power)) + ", mean: " + "{0:.4f}".format(np.mean(power)) + ", max: " + str(np.max(power)),
            horizontalalignment='center', verticalalignment='center', transform=plt.gca().transAxes)
        plt.grid(True)
        plt.show()
    else:
        print("Usage: " + sys.argv[0] + " radar.txt")
