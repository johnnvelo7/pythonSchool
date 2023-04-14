class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance - amount >= 0:
            self.balance -= amount
        else:
            self.balance -= 10
            print("Insufficient funds. A $10 overdraft penalty has been charged.")

    def add_interest(self, interest_rate):
        self.balance += self.balance * (interest_rate / 100)

# Create a bank account with a starting balance of $100
account = BankAccount(100)

# Deposit $50
account.deposit(50)

# Withdraw $200 (should result in an overdraft penalty)
account.withdraw(200)

# Add interest of 5%
account.add_interest(5)

# Check the current balance
print(account.balance) # 65
