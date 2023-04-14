class Customer:
    def __init__(self):
        self.purchases = 0
        self.discount_reached = False

    def make_purchase(self, amount):
        self.purchases += amount
        if self.purchases >= 100 and not self.discount_reached:
            self.discount_reached = True
            print("Discount reached! You will receive a $10 discount on your next purchase.")

    def discount_reached(self):
        return self.discount_reached

customer = Customer()
customer.make_purchase(90)
print(customer.discount_reached) # False
customer.make_purchase(20)
print(customer.discount_reached) # True
