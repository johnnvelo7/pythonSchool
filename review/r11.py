from random import randint

heads = 0
tails = 0
for i in range(1000):
    coin = randint(1,2)
    if coin == 1:
        heads += 1
    else:
        tails += 1
print("Heads =", heads)
print("Tails =", tails)