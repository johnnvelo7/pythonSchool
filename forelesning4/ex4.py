# ADDITION
def add(x, y):
    return x + y


#  SUBTRACTION
def subtract(x, y):
    return x - y


# MULTIPLICATION
def multiply(x, y):
    return x * y


# DIVISION
def divide(x, y):
    return x / y


print("Select an operation. \n '+' for addition \n '-' for subtraction \n '*' for multiplication \n '/' for division")

# This will take the input from the user
while True:
    userInput = input("Enter an operation: ")
    if userInput in ('+', '-', '*', '/'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number"))
        except ValueError:
            print("Invalid input. Please enter a number")
            continue

        if userInput == '+':
            print(f"{num1} + {num2} will be: ", add(num1, num2))
        elif userInput == '-':
            print(f"{num1} - {num2} will be: ", subtract(num1, num2))
        elif userInput == '*':
            print(f"{num1} * {num2} will be: ", multiply(num1, num2))
        elif userInput == '/':
            print(f"{num1} / {num2} will be: ", divide(num1, num2))

        next_calculation = input("You wanna try again? y/n: ")
        if next_calculation == 'n':
            break

    else:
        print("Invalid input")

    if userInput == 'q':
        break
