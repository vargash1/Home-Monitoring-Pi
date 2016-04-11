#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Vargas Hector <vargash1>
# @Date:   Sunday, April 10th 2016, 11:25:34 pm
# @Email:  vargash1@wit.edu
# @Last modified by:   vargash1
# @Last modified time: Sunday, April 10th 2016, 11:28:31 pm

import os
from setuptools import setup

# Utility function to read the README file.
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "vRaspi",
    version = "0.0.0",
    author = "Hector Vargas",
    author_email = "vargash1@wit.edu",
    description = ("vRaspi"),
    license = "MIT",
    url = "https://github.com/vargash1/vraspi",
    packages = ['vraspi'],
    package_dir = {'vraspi':'vraspi'},
    long_description = read('README.md'),
    # entry_points = {
    # 'console_scripts': [
    #     'arithcli=arithmos.arithcli:main',
    # ],
    # },
)
