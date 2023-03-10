# NESTE IF ELSE

RATE1 = 0.10
RATE2 = 0.25
RATE1_SINGLE_LIMIT = 32000
RATE1_MARRIED_LIMIT = 64000

income = float(input("Please enter your income: "))
marital_status = input("Please enter s for single, m for married: ")

tax1 = 0
tax2 = 0

if marital_status == 's':
    if income <= RATE1_SINGLE_LIMIT:
        tax1 = RATE1 * income
    else:
        tax1 = RATE1 * RATE1_SINGLE_LIMIT
        tax2 = RATE2 * (income - RATE1_SINGLE_LIMIT)

else:
    if income <= RATE1_MARRIED_LIMIT:
        tax1 = RATE1 * income
    else:
        tax1 = RATE1 * RATE1_MARRIED_LIMIT
        tax2 = RATE2 * (income - RATE1_MARRIED_LIMIT)

total_tax = tax1 + tax2

print("The Tax is $%.2f" % total_tax)
