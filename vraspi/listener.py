#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Vargas Hector <vargash1>
# @Date:   Sunday, April 10th 2016, 11:18:37 pm
# @Email:  vargash1@wit.edu
# @Last modified by:   vargash1
# @Last modified time: Monday, April 11th 2016, 4:38:43 am
import multiprocessing
from vraspi import ultrasonic, motion, light, temp, noise

class SensorListener:
    def __init__(self):
        self.msgqueue = None
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

    def getQueueMessage(self):
        return self.msgqueue.get()

    def execute(self):
        self.queue = multiprocessing.Queue()
        self.initialize()
        self.runProcesses()


def main():
    listener = SensorListener()
    listener.execute()

if __name__ == "__main__":
    main()
