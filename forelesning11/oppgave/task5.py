class MyCustomer:
    def __init__(self):
        self.purchase = 0
        self.discount_reached = False

    def make_purchase(self, amount):
        self.purchase += amount
        if self.purchase >= 100 and not self.discount_reached:
            self.discount_reached = True
            print("Discount reached! You will receive $10 discount on your next purchase.")

    def discount_reached(self):
        return self.discount_reached

customer = MyCustomer()
customer.make_purchase(90)
print(customer.discount_reached)
customer.make_purchase(20)
print(customer.discount_reached)

