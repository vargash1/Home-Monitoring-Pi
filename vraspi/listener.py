#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Vargas Hector <vargash1>
# @Date:   Sunday, April 10th 2016, 11:18:37 pm
# @Email:  vargash1@wit.edu
# @Last modified by:   vargash1
# @Last modified time: Monday, April 11th 2016, 2:55:37 am
import multiprocessing
from vraspi import ultrasonic, motion, light, temp, noise
import time


def main():
    ultratest = ultrasonic.UltraSonicSensor()
    motiontest = motion.MotionSensor()
    lighttest = light.LightSensor()
    temptest = temp.TempReader()
    soundtest = noise.NoiseSensor()
    p1 = multiprocessing.Process(target=motiontest.detect_Motion)
    p2 = multiprocessing.Process(target=ultratest.detect_dist)
    p3 = multiprocessing.Process(target=lighttest.detect_light)
    p4 = multiprocessing.Process(target=temptest.detect_temp)
    p5 = multiprocessing.Process(target=soundtest.detect_sound)
    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p5.start()

if __name__ == "__main__":
    main()
    while True:
        time.sleep(1)
