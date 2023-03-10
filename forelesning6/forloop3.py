#!/usr/bin/env python3

# for i in range(3):
#     for i in range(4):
#         print("*", end = " ")
#     print(" ")

for i in range(3):
    for j in range(5):
        if j % 2 == 1:
            print("*", end="")
        else:
            print("-", end="")
    print()

