#!/usr/bin python3

value = int(input("Enter a value: "))
user_input = input("Enter a value: ")

while user_input != "":
    previous = value
    value = int(user_input)
    if value == previous:
        print("Duplicate values.")
    user_input = input("Enter a value: ")