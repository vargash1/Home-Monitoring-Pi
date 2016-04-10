#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Vargas Hector <vargash1>
# @Date:   Saturday, April 9th 2016, 7:59:52 pm
# @Email:  vargash1@wit.edu
# @Last modified by:   vargash1
# @Last modified time: Saturday, April 9th 2016, 8:08:08 pm
import time
import picamera

class vRaspiCam:
    def __init__(self,ttl=1):
        self.camera = picamera.PiCamera()
        self.ttl = ttl
    def takeVid(self):
        try:
            camera.start_preview()
            time.sleep(self.ttl)
            camera.stop_preview()
        finally:
            camera.close()
def main():
    camtest = vRaspiCam()
    camera.takeVid()
if __name__ == "__main__":
    main()
