#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Vargas Hector <vargash1>
# @Date:   Saturday, April 9th 2016, 7:59:52 pm
# @Email:  vargash1@wit.edu
# @Last modified by:   vargash1
# @Last modified time: Saturday, April 9th 2016, 9:38:27 pm
import time
import picamera


class vRaspiCam:
    def __init__(self, ttl=1):
        self.camera = picamera.PiCamera()
        self.ttl = ttl

    def takeVid(self):
        try:
            self.camera.start_preview()
            time.sleep(self.ttl)
            self.camera.stop_preview()
        finally:
            print "kek"

    def takePic(self):
        self.camera.resolution = (2592, 1944)
        self.camera.start_preview()
        self.camera.exposure_compensation = 2
        self.camera.exposure_mode = 'spotlight'
        self.camera.meter_mode = 'matrix'
        self.camera.image_effect = 'gpen'
        # Give the cam some time to adjust to conditions
        time.sleep(2)
        try:
            self.camera.capture('foo.jpg')
            self.camera.stop_preview()
            self.camera.close()
        finally:
            print "lel"


def main():
    camtest = vRaspiCam()
    camtest.takeVid()
    camtest.takePic()

if __name__ == "__main__":
    main()
