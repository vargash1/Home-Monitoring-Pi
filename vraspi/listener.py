#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Vargas Hector <vargash1>
# @Date:   Sunday, April 10th 2016, 11:18:37 pm
# @Email:  vargash1@wit.edu
# @Last modified by:   vargash1
# @Last modified time: Monday, April 11th 2016, 3:05:54 pm
import multiprocessing
from vraspi import ultrasonic, motion, light, temp, noise, log

class SensorListener:
    def __init__(self, logger):
        self.msgqueue = None
        self.ultrasonicProcess = None
        self.motionProcess = None
        self.lightProcess = None
        self.tempProcess = None
        self.soundProcess = None
        self.logger = logger

    def initialize(self):
        ultratest = ultrasonic.UltraSonicSensor(self.msgqueue, self.logger)
        motiontest = motion.MotionSensor(self.msgqueue, self.logger)
        lighttest = light.LightSensor(self.msgqueue, self.logger)
        temptest = temp.TempReader(self.msgqueue, self.logger)
        soundtest = noise.NoiseSensor(self.msgqueue, self.logger)
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
        self.msgqueue = multiprocessing.Queue()
        self.initialize()
        self.runProcesses()


def main():
    lels = log.VRaspLog()
    lels.initLogger()

    listener = SensorListener(lels)
    listener.execute()
    while True:
        msg  = listener.getQueueMessage()
        if msg is not None:
            print msg
        else:
            print "No queue messages!"

if __name__ == "__main__":
    main()
