def integerPower(x,y):
    result = 1
    for i in range(y):
        result = result * x

    return result

x = int(input("Enter an integer: "))
y = int(input("Enter a positive, nonzero integer: "))

result = integerPower(x,y)

print(f"{x}^{y} = {result}")
