#!/usr/bin/env python3

# GLOBAL CONSTANTS
RMAX = 10
CMAX = 4

for i in range(1, CMAX + 1):
    print("%10d" % i, end="")

print()

for i in range(1, CMAX + 1):
    print("%9s" % "x ", end="")

print()
print("    ", "-" * 35)

for x in range(1, RMAX+1):
    for n in range(1, CMAX+1):
        print("%10d" % x**n, end="")
    print()
