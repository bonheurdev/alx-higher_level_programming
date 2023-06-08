#!/usr/bin/python3

import sys

m = len(sys.argv)
args = m - 1

if args == 0:
    print("{} arguments.".format(args))
elif args == 1:
    print("{} argument:".format(args)) 
else:
    print("{} arguments:".format(args))

for x in range(1, m):
    var1 = sys.argv[x]
    print("{}: {}".format(x, var1))
