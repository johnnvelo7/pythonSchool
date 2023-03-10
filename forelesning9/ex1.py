# TASK A

a = [1, 2, 3, 4, 5, 4, 3, 2, 1, 0]

total = 0
for i in range(10):
    total = total + a[i]

print(total)

# TASK B

a = [1, 2, 3, 4, 5, 4, 3, 2, 1, 0]

total = 0
for i in range(0, 10, 2):
    total = total + a[i]

print(total)

#  TASK C

a = [1, 2, 3, 4, 5, 4, 3, 2, 1, 0]

total = 0
for i in range(1, 10, 2):
    total = total + a[i]

print(total)

#  TASK D

a = [1, 2, 3, 4, 5, 4, 3, 2, 1, 0]

total = 0
for i in range(2, 10):
    total = total + a[i]
print(total)

#  TASK E

a = [1, 2, 3, 4, 5, 4, 3, 2, 1, 0]

total = 0
i = i
while i < 10:
    total = total + a[i]
    i = 2 * i
print(total)

#  TASK F

a = [1, 2, 3, 4, 5, 4, 3, 2, 1, 0]

total = 0
for i in range(9, -1, -1):
    total = total + a[i]
print(total)

#  TASK G

a = [1, 2, 3, 4, 5, 4, 3, 2, 1, 0]

total = 0
for i in range(-9, -1, -2):
    total = total + a[i]
print(total)

#  TASK H

a = [1, 2, 3, 4, 5, 4, 3, 2, 1, 0]

total = 0
for i in range(0, 10):
    total = a[i] - total
print(total)
