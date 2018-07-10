#!/usr/bin/env python
from setuptools import setup, find_packages
import os

# This simulates a requirement which is not necessary in the wheel
# But needed if building from source
if 'BUILDING_WHEEL' not in os.environ:
    raise Exception("Fake build error")

setup(name='wheel_only',
      version='1.0',
      packages=find_packages()
      )
