from random import random, randint, uniform

for i in range(10):
    number = random()
    print("%.2f" % number)

print()

for i in range(10):
    num_int = randint(10, 100)
    print(num_int)

print()

for i in range(10):
 num_float = uniform(-10, 10)
 print("%.2f" % num_float)

