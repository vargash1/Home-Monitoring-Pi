#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Vargas Hector <vargash1>
# @Date:   Monday, April 11th 2016, 12:10:05 am
# @Email:  vargash1@wit.edu
# @Last modified by:   vargash1
# @Last modified time: Monday, April 11th 2016, 3:49:26 am
import grovepi
import time
import sys

class LightSensor:

    def __init__(self, queue):
        # GrovePi Analog Port
        self.port = 1
        self.threshold = 10
        self.msgq = queue


    def detect_light(self):
        while True:
            try:
                time.sleep(6)
                val = grovepi.analogRead(self.port)
                resistance = float(1023 - val) * 10 / val
                if resistance > self.threshold:
                    print "Low Light Levels"
                else:
                    print "High Light Levels"
                print "sensor val: {} resistance: {}".format(val, resistance)
                sys.stdout.flush()

            except IOError:
                pass
