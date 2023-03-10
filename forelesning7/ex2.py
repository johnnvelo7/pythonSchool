def factorial(n):
    fact = 1

    while n >= 1:
        fact = fact * n
        n = n -1
    return fact

n = int(input("Enter n to calculate factorial: "))
if n < 0:
    print("Factorial is not defined for negative numbers.")
else:
    fact = factorial(n)
    print(f"{n}!= {fact}")
