#!/usr/bin/env python3

# BALANCE ACCOUNT

# CONSTANT VALUE OF RATE AND INITIAL BALANCE
RATE = 0.05
INITIALIZE_BALANCE = 10000

num_years = int(input("Enter the number of years: "))
balance = INITIALIZE_BALANCE

print("%5s %12s" % ("Year", "BALANCE"))
print("-" * 20)

for year in range(1, num_years+1):
    interest = balance * RATE
    balance = balance + interest
    print("%3d %14.2f" % (year, balance))