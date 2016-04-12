#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Vargas Hector <vargash1>
# @Date:   Wednesday, March 16th 2016, 9:20:48 am
# @Email:  vargash1@wit.edu
# @Last modified by:   vargash1
# @Last modified time: Tuesday, April 12th 2016, 5:05:50 am
from datetime import datetime
import grovepi
import time
import sys

class NoiseSensor:
    def __init__(self, queue, logger):
        # analog
        self.soundsensor = 0
        self.soundthreshold = 400
        self.msgq = queue
        self.logger = logger
    def detect_sound(self):
        while True:
            try:
                time.sleep(5)
                soundval = grovepi.analogRead(self.soundsensor)
                nowt = datetime.now()
                if soundval > self.soundthreshold:
                    # weird bug
                    if soundval < 1000:
                        strmsg = "High sound levels detected"
                        self.msgq.put({"sound":strmsg,"time":nowt.strftime('%m-%d-%Y_%H:%M:%S')})
                else:
                    self.logger.logInfo("Low Sound levels {}".format(nowt.strftime('%m-%d-%Y_%H:%M:%S')))                    
                sys.stdout.flush()
            except IOError:
                pass
