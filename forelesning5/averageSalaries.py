#!/usr/bin python3

total = 0
count = 0

salary = float(input("Enter a salary or -1 to finish: "))

while salary >= 0.0:
    total += salary
    count += 1
    salary = float(input("Enter a salary or -1 to finish: "))

if count > 0:
    average = total / count
    print(f"Average Salary is: {average}")
else:
    print("Please enter a valid salary.")
