#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Vargas Hector <vargash1>
# @Date:   Sunday, April 10th 2016, 6:21:12 pm
# @Email:  vargash1@wit.edu
# @Last modified by:   vargash1
# @Last modified time: Sunday, April 10th 2016, 9:11:13 pm
import grovepi

class UltraSonicSensor:

    def __init__(self):
        # Grovepi Sensor Connection
        self.ranger = 4

    def detect_dist(self):
        while True:
            try:
                dist = grovepi.ultrasonicRead(self.ranger)
                print "Dist: {}".format(dist)
            except TypeError:
                pass
            except IOError:
                pass
def main():
    test = UltraSonicSensor()
    test.detect_dist()

if __name__ == "__main__":
    main()
