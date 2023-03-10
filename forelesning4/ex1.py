#!usr/bin/env python3
from math import sqrt

# 1
print("TASK 1.a\n")
n = 1
m = -1
if n < -m:
    print(n)
else:
    print(m)

# 2
print("TASK 1.b\n")
n = 1
m = -1
if -n >= m:
    print(n)
else:
    print(m)

# 3
print("TASK 1.c\n")
x = 0.0
y = 1.0
if abs(x-y) < 1:
    print(x)
else:
    print(y)

# 4
print("TASK 1.d")
x = sqrt(2.0)
y = 2.0
if x * x == y:
    print(x)
else:
    print(y)


