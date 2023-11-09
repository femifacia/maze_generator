#!/usr/bin/env python

import sys
sys.path.append('./src')
from core import Core

if __name__ == '__main__':
    core = Core(500, 500)
    core.run()

