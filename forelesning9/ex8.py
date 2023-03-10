import random

def sum_without_smallest():
    values = [random.randint(1, 100) for _ in range(10)]

    s = values [0]
    smallest = values [0]

    for v in values[1:]:
        s += v
        if v < smallest:
            smallest = v

    return s - smallest

