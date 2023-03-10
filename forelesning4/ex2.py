#!usr/bin/env python3

userInput = int(input("Please enter a number between 1 and 10: "))

if userInput > 10:
    print(f"The number: {userInput} is greater than 10.")
elif userInput < 1:
    print(f"The number: {userInput} is less than 1.")
else:
    print(f"The number: {userInput} is between 1 and 10.")

