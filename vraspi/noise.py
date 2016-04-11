#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Vargas Hector <vargash1>
# @Date:   Wednesday, March 16th 2016, 9:20:48 am
# @Email:  vargash1@wit.edu
# @Last modified by:   vargash1
# @Last modified time: Monday, April 11th 2016, 2:49:29 am
import grovepi
import time
import sys

class NoiseSensor:
    def __init__(self):
        # analog
        self.soundsensor = 0
        self.soundthreshold = 400
    def detect_sound(self):
        while True:
            try:
                time.sleep(2)
                soundval = grovepi.analogRead(self.soundsensor)
                if soundval > self.soundthreshold:
                    print "no sound"
                else:
                    print "sound higher than thresh"
                sys.stdout.flush()
            except IOError:
                pass
