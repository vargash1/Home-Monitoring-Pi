#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Vargas Hector <vargash1>
# @Date:   Sunday, April 10th 2016, 11:18:37 pm
# @Email:  vargash1@wit.edu
# @Last modified by:   vargash1
# @Last modified time: Monday, April 11th 2016, 4:02:17 am
import multiprocessing
from vraspi import ultrasonic, motion, light, temp, noise
import time

class SensorListener:
    def __init__(self, queue):
        self.msgqueue = queue
        self.ultrasonicProcess = None
        self.motionProcess = None
        self.lightProcess = None
        self.tempProcess = None
        self.soundProcess = None

    def initialize(self):
        ultratest = ultrasonic.UltraSonicSensor(self.msgqueue)
        motiontest = motion.MotionSensor(self.msgqueue)
        lighttest = light.LightSensor(self.msgqueue)
        temptest = temp.TempReader(self.msgqueue)
        soundtest = noise.NoiseSensor(self.msgqueue)
        self.motionProcess = multiprocessing.Process(target=motiontest.detect_Motion)
        self.ultrasonicProcess = multiprocessing.Process(target=ultratest.detect_dist)
        self.lightProcess = multiprocessing.Process(target=lighttest.detect_light)
        self.tempProcess = multiprocessing.Process(target=temptest.detect_temp)
        self.soundProcess = multiprocessing.Process(target=soundtest.detect_sound)

    def runProcesses(self):
        self.ultrasonicProcess.start()
        self.motionProcess.start()
        self.lightProcess.start()
        self.tempProcess.start()
        self.soundProcess.start()

    def getQueueMessages(self):
        while True:
            msg = self.msgqueue.get()
            if msg is not None:
                print msg

def main():
    queue = multiprocessing.Queue()
    listener = SensorListener(queue)
    listener.initialize()
    listener.runProcesses()
    listener.getQueueMessages()

if __name__ == "__main__":
    main()
