#!/usr/bin python3

user_input = input("Enter a number: ")
while user_input.isascii():
    value = float(user_input)
    print(value)
    user_input = input("Enter a number: ")

