#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Vargas Hector <vargash1>
# @Date:   Sunday, April 10th 2016, 11:18:37 pm
# @Email:  vargash1@wit.edu
# @Last modified by:   vargash1
# @Last modified time: Monday, April 11th 2016, 12:26:28 am
import multiprocessing
from vraspi import ultrasonic, motion, light
import time


def main():
    ultratest = ultrasonic.UltraSonicSensor()
    motiontest = motion.MotionSensor()
    lighttest = light.LightSensor()
    p1 = multiprocessing.Process(target=motiontest.detect_Motion)
    p2 = multiprocessing.Process(target=ultratest.detect_dist)
    p3 = multiprocessing.Process(target=lighttest.detect_light)
    p1.start()
    p2.start()
    p3.start()

if __name__ == "__main__":
    main()
    while True:
        time.sleep(1)
