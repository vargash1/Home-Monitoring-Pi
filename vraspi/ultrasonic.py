#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Vargas Hector <vargash1>
# @Date:   Sunday, April 10th 2016, 6:21:12 pm
# @Email:  vargash1@wit.edu
# @Last modified by:   vargash1
# @Last modified time: Monday, April 11th 2016, 3:08:13 pm
from datetime import datetime
import grovepi
import time
import sys

class UltraSonicSensor:

    def __init__(self, queue logger):
        # Grovepi Digital Port
        self.ranger = 4
        self.msgq = queue
        self.logger = logger


    def detect_dist(self):
        while True:
            try:
                dist = grovepi.ultrasonicRead(self.ranger)
                if dist < 300:
                    nowt = datetime.now()
                    self.msgq.put("Ultrasonic detected object distance: {}".format(dist))
                    self.msgq.put("Ultrasonic detection at: {}".format(nowt.strftime('%m-%d-%Y_%H:%M:%S')))
                    sys.stdout.flush()
            except TypeError:
                pass
            except IOError:
                pass
            time.sleep(3)
def main():
    test = UltraSonicSensor()
    test.detect_dist()

if __name__ == "__main__":
    main()
