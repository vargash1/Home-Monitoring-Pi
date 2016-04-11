#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Vargas Hector <vargash1>
# @Date:   Monday, April 11th 2016, 12:10:05 am
# @Email:  vargash1@wit.edu
# @Last modified by:   vargash1
# @Last modified time: Monday, April 11th 2016, 10:29:21 am
from datetime import datetime
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
                if val < 700:
                    nowt = datetime.now()
                    self.msgq.put("Light val: {} resistance: {}".format(val, resistance))
                    self.msgq.put("Light reading taken at {}".format(nowt.strftime('%m-%d-%Y_%H:%M:%S')))
                sys.stdout.flush()

            except IOError:
                pass
