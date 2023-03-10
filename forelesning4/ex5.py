# Weight checker for KG or LBS

# DEFINE VALUES
def kgToLbs(x):
    return x * 2.2


def lbsToKg(x):
    return x * 0.4


# Formula = 1 kg = 2.2 lbs | 1 lbs = 0.45 kg

print("Please enter an option that you want to use. KG for Kilogram and LBS for Pounds.")

while True:
    userInput = input("Enter an option: ")
    if userInput in ("KG", "LBS", "kg", "lbs", "kilogram", "pounds"):
        try:
            number = float(input("Enter the number: "))
        except ValueError:
            print("Invalid input. Please enter a number")
            continue

        if userInput == "KG" or "kg" or "kilogram":
            print(f"{number} KG in LBS is: ", kgToLbs(number))
        elif userInput == "LBS" or "lbs" or "pounds":
            print(f"{number} LBS in KG is: ", lbsToKg(number))

        next_calculation = input("You wanna try again? y/n: ")
        if next_calculation == 'n':
            break
    else:
        print("Invalid input")



# Number checker if valid
# if userInput.isdigit():
#     number = int(userInput)
#     print(number)
# else:
#     print("You did not insert a valid number.")
#
# if userInput1.replace(".", "").isdigit():
#     number2 = float(userInput2)
#     print(number2)
# else:
#     print("You did not insert a valid number.")
