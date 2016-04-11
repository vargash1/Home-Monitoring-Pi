#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Vargas Hector <vargash1>
# @Date:   Monday, April 11th 2016, 12:10:05 am
# @Email:  vargash1@wit.edu
# @Last modified by:   vargash1
# @Last modified time: Monday, April 11th 2016, 12:48:03 am
import grovepi
import time
import sys

class LightSensor:

    def __init__(self):
        # GrovePi Analog Port
        self.port = 1
        self.threshold = 10

    def detect_light(self):
        while True:
            try:
                val = grovepi.analogRead(self.port)
                resistance = float(1023 - val) * 10 / val
                if resistance > self.threshold:
                    print "Low Light Levels"
                else:
                    print "High Light Levels"
                print "sensor val: {} resistance: {}".format(val, resistance)
                sys.stdout.flush()
                time.sleep(3)
            except IOError:
                pass
