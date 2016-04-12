#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Vargas Hector <vargash1>
# @Date:   Wednesday, March 16th 2016, 9:20:48 am
# @Email:  vargash1@wit.edu
# @Last modified by:   vargash1
# @Last modified time: Tuesday, April 12th 2016, 2:22:24 am
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
                time.sleep(2)
                soundval = grovepi.analogRead(self.soundsensor)
                nowt = datetime.now()
                if soundval > self.soundthreshold:
                    self.logger.logInfo("Low Sound levels {}".format(nowt.strftime('%m-%d-%Y_%H:%M:%S')))
                else:
                    # weird bug
                    if soundval < 1000:
                        strmsg = "High sound levels detected: {} {}".format(soundval,nowt.strftime('%m-%d-%Y_%H:%M:%S'))
                        self.msgq.put({"sound":strmsg})
                sys.stdout.flush()
            except IOError:
                pass
