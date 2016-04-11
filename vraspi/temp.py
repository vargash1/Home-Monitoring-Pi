#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Vargas Hector <vargash1>
# @Date:   Wednesday, March 16th 2016, 9:20:59 am
# @Email:  vargash1@wit.edu
# @Last modified by:   vargash1
# @Last modified time: Monday, April 11th 2016, 2:01:57 am
import grovepi
import time
import sys

class TempReader:

    def __init__(self):
        self.temport = 7
        self.senseType = 0

    def detect_temp(self):
        while True:
            try:
                time.sleep(5)
                [temp,humi] = grovepi.dht(self.temport,self.senseType)
                print "Temp: {} C\tHumidity:{}".format(temp,humi)
                sys.stdout.flush()
            except IOError:
                pass
            except TypeError:
                raise
