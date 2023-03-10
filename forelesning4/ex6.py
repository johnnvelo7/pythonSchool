#!/usr/bin/env python3

string = input("Please enter a text: ")

# contains only letters
# contains only uppercase letters
# contains only lowercase letters
# contains only digits
# contains only letters and digits
# starts with an uppercase
# ends with a period

print(string.isalnum())
print(string.isdigit())
print(string.endswith("."))
print(string.capitalize())
print(string.isspace())
print(string.islower())
print(string.isupper())