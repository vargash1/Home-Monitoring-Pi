#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Vargas Hector <vargash1>
# @Date:   Saturday, April 9th 2016, 7:59:52 pm
# @Email:  vargash1@wit.edu
# @Last modified by:   vargash1
# @Last modified time: Tuesday, April 12th 2016, 6:06:29 am
import time
import picamera


class vRaspiCam:
    def __init__(self, ttl=1):
        self.camera = picamera.PiCamera()
        self.ttl = ttl

    """Takes a vid"""
    def take_Vid(self):
        try:
            self.camera.start_preview()
            time.sleep(self.ttl)
            self.camera.stop_preview()
        finally:
            print "kek"

    """Takes a picture"""
    def take_Pic(self):
        self.camera.resolution = (2592, 1944)
        camera.start_preview()
        time.sleep(2)
        # Give the cam some time to adjust to conditions
        try:
            self.camera.capture('foo.jpg')
        finally:
            print "lel"


def main():
    camtest = vRaspiCam()
    # camtest.take_Vid()
    camtest.take_Pic()

if __name__ == "__main__":
    main()
