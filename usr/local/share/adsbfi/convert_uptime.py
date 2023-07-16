#!/usr/bin/python3

import sys
from datetime import *

if len(sys.argv) > 1:
    s = timedelta(seconds=float(sys.argv[1]))
    d = datetime(1,1,1) + s
    print("%dd %02dh %02dm %02ds" % (d.day-1, d.hour, d.minute, d.second))
else:
    print("%dd %02dh %02dm %02ds" % (0, 0, 0, 0))
