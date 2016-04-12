#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Vargas Hector <vargash1>
# @Date:   Wednesday, March 16th 2016, 9:20:59 am
# @Email:  vargash1@wit.edu
# @Last modified by:   vargash1
# @Last modified time: Tuesday, April 12th 2016, 2:13:07 am
from datetime import datetime
import grovepi
import math
import time
import sys

class TempReader:

    def __init__(self, queue, logger):
        self.temport = 7
        self.senseType = 0
        self.msgq = queue
        self.logger = logger



    def detect_temp(self):
        while True:
            try:
                time.sleep(5)
                [temp,humi] = grovepi.dht(self.temport, self.senseType)
                if not (math.isnan(temp) or math.isnan(humi)):
                    temp = (temp * 9/5) + 32
                    nowt = datetime.now()
                    strmsg = "Temperature: {} F\tHumidity:{}".format(temp, humi)
                    self.logger.logInfo("{} {}".format(strmsg,nowt.strftime('%m-%d-%Y_%H:%M:%S')))
                    self.msgq.put({"temp":strmsg})
                    sys.stdout.flush()
            except IOError:
                pass
            except TypeError:
                raise
