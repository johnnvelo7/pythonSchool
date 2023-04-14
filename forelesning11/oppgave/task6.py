class MyBankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance - amount >= 0:
            self.balance -= amount
        else:
            self.balance -= 10
            print("Insufficient funds.")

    def add_interest(self, interest_rate):
        self.balance += self.balance * (interest_rate / 100)

account = MyBankAccount(100)
account.deposit(50)
account.withdraw(200)
account.add_interest(5)
print(account.balance)