#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Vargas Hector <vargash1>
# @Date:   Wednesday, March 16th 2016, 9:20:36 am
# @Email:  vargash1@wit.edu
# @Last modified by:   vargash1
# @Last modified time: Tuesday, April 12th 2016, 2:16:22 am
import time
import sys
import grovepi
from datetime import datetime

class MotionSensor:

    def __init__(self, queue, logger):
        # Grovepi Digital Port
        self.pir_sensor = 8
        self.msgq = queue
        self.logger = logger


    """ Dectects motion """
    def detect_Motion(self):
        grovepi.pinMode(self.pir_sensor, "INPUT")
        while True:
            try:
                motion = grovepi.digitalRead(self.pir_sensor)
                self.logger.logInfo("Motion sensor picked up motion")
                if motion == 0 or motion == 1:
                    nowt = datetime.now()
                    if motion == 1:
                        strmsg = "Movement Detected {}".format(nowt.strftime('%m-%d-%Y_%H:%M:%S'))
                        self.logger.logInfo(strmsg)
                        self.msgq.put({'motion':strmsg})
                    else:
                        self.logger.logInfo("No Motion {}".format(nowt.strftime('%m-%d-%Y_%H:%M:%S')))

                time.sleep(3)
            except IOError:
                print "IO err"
                pass
            sys.stdout.flush()


def main():
    # test = MotionSensor(0)
    # test.detect_Motion()
    print "EleGiggle"

if __name__ == "__main__":
    main()
