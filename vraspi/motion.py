#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Vargas Hector <vargash1>
# @Date:   Wednesday, March 16th 2016, 9:20:36 am
# @Email:  vargash1@wit.edu
# @Last modified by:   vargash1
# @Last modified time: Monday, April 11th 2016, 4:03:05 am
import time
import sys
import grovepi

class MotionSensor:

    def __init__(self, queue):
        # Grovepi Digital Port
        self.pir_sensor = 8
        self.msgq = queue


    """ Dectects motion """
    def detect_Motion(self):
        grovepi.pinMode(self.pir_sensor, "INPUT")
        mode = 0
        while True:
            try:
                motion = grovepi.digitalRead(self.pir_sensor)
                if motion == 0 or motion == 1:
                    if motion == 1:
                        mode = 1
                        print "Detection"
                        self.msgq.put("Motion Detected")
                    else:
                        mode = 0
                        print "--"
                time.sleep(3)
            except IOError:
                print "IO err"
                pass
            sys.stdout.flush()


def main():
    test = MotionSensor(0)
    test.detect_Motion()

if __name__ == "__main__":
    main()
