RAISE_FACTOR = 2400.00
UNACCEPTABLE = 0
ACCEPTABLE = 0.4
MERITORIOUS = 0.6

rating = float(input("Enter the rating: "))
if rating == UNACCEPTABLE:
    performance = "Unacceptable"
elif rating == ACCEPTABLE:
    performance = "Acceptable"
elif rating == MERITORIOUS:
    performance = "Meritorious"
else:
    performance = ""

if performance == "":
    print("That was not a valid rating.")
else:
    print("Based on that rating, your performance is", performance)
    print("You will recieve a raise of $%.2f." % (rating * RAISE_FACTOR))