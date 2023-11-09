#!/usr/bin/env python

import sys
sys.path.append('./src')
from core import Core

if __name__ == '__main__':
    # our core system
    core = Core(500, 500)
    # we run on our core
    core.run()

