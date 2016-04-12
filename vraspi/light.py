#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Vargas Hector <vargash1>
# @Date:   Monday, April 11th 2016, 12:10:05 am
# @Email:  vargash1@wit.edu
# @Last modified by:   vargash1
# @Last modified time: Tuesday, April 12th 2016, 3:38:07 am
from datetime import datetime
import grovepi
import time
import sys

class LightSensor:

    def __init__(self, queue, logger):
        # GrovePi Analog Port
        self.port = 1
        self.threshold = 10
        self.msgq = queue
        self.logger = logger



    def detect_light(self):
        while True:
            try:
                time.sleep(6)
                val = grovepi.analogRead(self.port)
                resistance = float(1023 - val) * 10 / val
                nowt = datetime.now()
                if resistance > self.threshold:
                    self.logger.logInfo("Low Light Levels {}".format(nowt.strftime('%m-%d-%Y_%H:%M:%S')))

                else:
                    if val < 700:
                        strmsg = "High Light Levels"
                        self.msgq.put({"light":strmsg,"time":nowt.strftime('%m-%d-%Y_%H:%M:%S')})
                        sys.stdout.flush()

            except IOError:
                pass
