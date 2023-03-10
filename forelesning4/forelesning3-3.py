# ELSE IF

richterScale = float(input("Enter a magnitude on the Richter scale: "))

if richterScale >= 8.0:
    print("Most structures fall")
elif richterScale >= 7.0:
    print("Many buildings destroyed")
elif richterScale >= 6.0:
    print("Many buildings considerably destroyed")
elif richterScale >= 4.5:
    print("Damage to poorly buildings")
else:
    print("No destruction of buildings")