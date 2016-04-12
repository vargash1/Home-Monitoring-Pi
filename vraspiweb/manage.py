#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Vargas Hector <vargash1>
# @Date:   Wednesday, March 16th 2016, 9:52:36 am
# @Email:  vargash1@wit.edu
# @Last modified by:   vargash1
# @Last modified time: Tuesday, April 12th 2016, 2:30:25 am

import os
import sys
import dotenv

if __name__ == "__main__":
    dotenv.read_dotenv()
    
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "vraspiweb.settings")
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
