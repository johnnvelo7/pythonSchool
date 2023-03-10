def multiple(a,b):
    if b % a == 0:
        return True
    else:
        return False

number1 = int(input("Enter a number: "))
number2 = int(input("Enter another number: "))

result = multiple(number1, number2)

if result:
    print(f"{number2} is a multiple of {number1}")
else:
    print(f"{number2} is NOT a multiple of {number1}")
