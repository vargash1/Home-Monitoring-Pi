#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Vargas Hector <vargash1>
# @Date:   Monday, April 11th 2016, 1:34:26 pm
# @Email:  vargash1@wit.edu
# @Last modified by:   vargash1
# @Last modified time: Monday, April 11th 2016, 2:41:14 pm
import logging
import time
import sys
import os
import stat
import errno
import coloredlogs
from datetime import datetime

class VRaspLog:

    def __init__(self):
        self.fp = None
        self.logpath = self.get_logpath()
        self.logfile = None
        self.logger = None
        self.dt = datetime.now()

    def get_logpath(self):
        # /home/user/.vraspi
        logpath = os.path.join(os.path.expanduser("~"), ".vraspi")

        # Check to see if directory doesnt exist
        try:
            direxists = stat.S_ISDIR(os.stat(logpath).st_mode)
        except OSError,e:
            # If directory doesn't exist, lets create it
            if e.errno == errno.ENOENT:
                try:
                    os.mkdir(logpath)
                # Raise other errors besides ENOENT
                except OSError:
                    raise
                return logpath
            else:
                raise
        if (direxists):
            return logpath
    """
    Creates a log file based on date and current time
    in our hidden directory as created by self.getLogPath()
    """
    def getLogFile(self):
        tmp = datetime.now()
        kek = ("log_{}".format(tmp.strftime('%m_%d_%Y_%H_%M_%S')))
        filepath = os.path.join(self.logpath, kek)
        try:
            fd = open(filepath,'w+')
        except IOError:
            raise
        fd.close()
        self.fp = filepath

    """
    Logs info that is ok with Arithmos execution
    """
    def logInfo(self,msg=""):
        self.logger.info(msg)

    """
    Logs info that can lead to Arithmos breaking execution
    """
    def logErr(self,msg=""):
        self.logger.error(msg)

    """
    Logs info that won't break Arithmos execution,
    but might lead to unexpected behavior
    """
    def logWarn(self,msg=""):
        self.logger.warning(msg)

    """
    Logs debug info only.
    """
    def logDebug(self,msg=""):
        self.logger.debug(msg)

    """
    Logs critical error information that will break Arithmos execution
    """
    def logCrit(self,msg=""):
        self.logger.critical(msg)

    """
    Creates two handlers for logging
    One to self.filepath
    One to STDOUT
    """
    def initLogger(self):
        self.getLogFile()
        logger = logging.getLogger('vRaspi')
        coloredlogs.install(level='DEBUG')

        # File IO Logging
        logfh = logging.FileHandler(self.fp)
        logfh.setLevel(logging.DEBUG)

        # STDOUT Logging
        logch = logging.StreamHandler()
        logch.setLevel(logging.DEBUG)

        # Format the output of both loggers
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        logfh.setFormatter(formatter)
        logch.setFormatter(formatter)

        # Make sure we add the handlers to our logger object
        logger.addHandler(logch)
        logger.addHandler(logfh)
        self.logger = logger

def main():
    test = VRaspLog()
    kek = test.get_logpath()
    test.initLogger()
    test.logInfo("kekekek")
if __name__ == "__main__":
    main()
