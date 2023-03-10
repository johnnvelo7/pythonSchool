from math import sqrt

def f(x):
    return g(x) + sqrt(h(x))
def g(x):
    return 4 * h(x)
def h(x):
    return x * x + k(x) -1
def k(x):
    return 2 * (x + 1)

x1 = f(2)
print("X1 =", x1)
x2 = g(h(2))
print("X2 =", x2)
x3 = k(g(2) + h(2))
print("X3 =", x3)
x4 = f(0) + f(1) + f(2)
print("X4 =", x4)
x5 = f(-1) + g(-1) + h(-1) + k(-1)
print("X5 =", x5)
