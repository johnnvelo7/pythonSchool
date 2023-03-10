# BOOLEAN VARIABLE

a = True
#  if a is TRUE then you can just write "a" on if statement

if a:
    print("Hi")
else:
    print("Bye")


#--------------------------------------------------------


string1 = "Python"
print("tho" in string1)
#  in operator can be used to check sub string inside the string


# -------------------------------------------------------

string2 = "Python Programming"
print(string2.count(string2))

# ---------------------------

string3 = "Python Programming"
print(string3.find("P"))

# ----------------------------

string4 = "Python Programming"
print(string4.endswith("g"))

#  ---------------------------

string5 = "PGR107"
print(string5.isalnum())

#  ------------------------------

string6 = "PGR107"
print(string6.isalpha())

#  ------------------------------

string7 = "PGR107"
print(string7.isdigit())

# --------------------------------

string8 = "       "
print(string8.isspace())


#  -------------------------------

userInput = input("Enter a number: ")

if userInput.isdigit():
    number = int(userInput)
    print(number)
else:
    print("You did not insert a valid number.")

#  -------------------------------------

userInput2 = input("Enter a floating point number: ")

if userInput2.replace(".", "").isdigit():
    number2 = float(userInput2)
    print(number2)
else:
    print("You did not insert a valid number.")