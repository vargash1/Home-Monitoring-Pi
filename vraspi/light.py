#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Vargas Hector <vargash1>
# @Date:   Monday, April 11th 2016, 12:10:05 am
# @Email:  vargash1@wit.edu
# @Last modified by:   vargash1
# @Last modified time: Monday, April 11th 2016, 12:29:13 am
import grovepi
import time

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
                    print "Resistance higher than threshold!"
                print "sensor val: {} resistance: {}".format(val, resistance)
                time.sleep(3)
            except IOError:
                pass
