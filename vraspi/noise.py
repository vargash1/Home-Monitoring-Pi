#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Vargas Hector <vargash1>
# @Date:   Wednesday, March 16th 2016, 9:20:48 am
# @Email:  vargash1@wit.edu
# @Last modified by:   vargash1
# @Last modified time: Monday, April 11th 2016, 10:23:21 am
from datetime import datetime
import grovepi
import time
import sys

class NoiseSensor:
    def __init__(self, queue):
        # analog
        self.soundsensor = 0
        self.soundthreshold = 400
        self.msgq = queue
    def detect_sound(self):
        while True:
            try:
                time.sleep(2)
                soundval = grovepi.analogRead(self.soundsensor)
                if soundval > self.soundthreshold:
                    print "low sound"
                    self.msgq.put("Low sound levels detected: {}".format(soundval))
                else:
                    print "sound higher than thresh"
                    nowt = datetime.now()
                    self.msgq.put("High sound levels detected: {}".format(soundval))
                self.msgq.put("Sound level taken at: {}".format(nowt.strftime('%m-%d-%Y_%H:%M:%S')))
                sys.stdout.flush()
            except IOError:
                pass
