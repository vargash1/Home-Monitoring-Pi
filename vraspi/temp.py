#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Vargas Hector <vargash1>
# @Date:   Wednesday, March 16th 2016, 9:20:59 am
# @Email:  vargash1@wit.edu
# @Last modified by:   vargash1
# @Last modified time: Monday, April 11th 2016, 10:17:39 am
from datetime import datetime
import grovepi
import math
import time
import sys

class TempReader:

    def __init__(self, queue):
        self.temport = 7
        self.senseType = 0
        self.msgq = queue


    def detect_temp(self):
        while True:
            try:
                time.sleep(5)
                [temp,humi] = grovepi.dht(self.temport, self.senseType)
                if not (math.isnan(temp) or math.isnan(humi)):
                    temp = (temp * 9/5) + 32
                    nowt = datetime.now()
                    self.msgq.put("Temperature: {} F\tHumidity:{}".format(temp, humi))
                    self.msgq.put("Temperature taken at: {}".format(nowt.strftime('%m-%d-%Y_%H:%M:%S')))
                    sys.stdout.flush()
            except IOError:
                pass
            except TypeError:
                raise
