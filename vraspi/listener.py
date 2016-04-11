#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Vargas Hector <vargash1>
# @Date:   Sunday, April 10th 2016, 11:18:37 pm
# @Email:  vargash1@wit.edu
# @Last modified by:   vargash1
# @Last modified time: Sunday, April 10th 2016, 11:31:20 pm
import multiprocessing
from vraspi import ultrasonic, motion
import time


def main():
    ultratest = ultrasonic.UltraSonicSensor()
    motiontest = motion.MotionSensor()

    p1 = multiprocessing.Process(motiontest.detect_Motion)
    p2 = multiprocessing.Process(ultratest.detect_dist)
    p1.start()
    p2.start()

if __name__ == "__main__":
    main()
    while True:
        time.sleep(1)
