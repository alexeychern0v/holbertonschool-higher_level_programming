#!/usr/bin/python3
for n in range(100):
    if (n != 99):
        print("{:02d}".format(n), end=", ")
    else:
        print("{0}".format(n), end = "\n")
