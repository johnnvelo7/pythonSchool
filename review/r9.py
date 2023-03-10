SENIOR_SALARY = 800
JUNIOR_SALARY = 375

status = input("Please enter the status of the salesperson (s/j): ")

if status.lower() == "s":
    print(f"The salary of the senior salesperson is ${SENIOR_SALARY} per week")
elif status.lower() == "j":
    print(f"The salary of the junior salesperson is ${JUNIOR_SALARY} per week")
else:
    print("Invalid input.")