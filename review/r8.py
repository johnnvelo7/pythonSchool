PAY_RATE = 8
EXTRA_PAY_RATE = 12

hours = int(input("Please enter the hours worked: "))
if hours < 0:
    print("Invalid input.")
elif hours <= 40:
    salary = hours * PAY_RATE
else:
    salary = 320 + (hours - 40) * EXTRA_PAY_RATE
print(f"Your salary is: {salary} dollars.")