# WHILE LOOP

x = 1
while x <= 5:
    y = 1 + x + (x ** 2)/2 + (x ** 3)/6 + (x ** 4)/24
    print(f"x = {x} -- > f(x) = {y : .2f}")
    x = x +1

# FOR LOOP

for x in range(1,6):
    y = 1 + x + (x ** 2) / 2 + (x ** 3)/6 + (x ** 4)/24
    print(f"x = {x} --> f(x) = {y : .2f}")