#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Vargas Hector <vargash1>
# @Date:   Saturday, April 9th 2016, 7:59:52 pm
# @Email:  vargash1@wit.edu
# @Last modified by:   vargash1
# @Last modified time: Tuesday, April 12th 2016, 6:55:32 am
import os
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
        time.sleep(2)
        # Give the cam some time to adjust to conditions
        try:
            fp = open("new_img.jpg",'wb')
            with self.camera as cam:
                cam.start_preview()
                time.sleep(1)
                cam.capture(fp)
        finally:
            print "Sucess"
        return os.path.abspath("new_img.jpg")


def main():
    camtest = vRaspiCam()
    # camtest.take_Vid()
    camtest.take_Pic()

if __name__ == "__main__":
    main()
