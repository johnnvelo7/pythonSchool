class MyAddress:
    def __init__(self, house_number, street, city, state, postal_code, apartment_number=None):
        self.house_number = house_number
        self.street = street
        self.city = city
        self.state = state
        self.postal_code = postal_code
        self.apartment_number = apartment_number

    # overriding the print statement
    def __str__(self):
        address = f"{self.house_number} {self.street}"
        # If there is an apartment number
        if self.apartment_number:
            address += f", Apartment number: {self.apartment_number}"
        address += f"\n{self.city}, {self.state} {self.postal_code}"
        return address

    # def comesbefore to sort
    def comesBefore(self, other):
        return self.postal_code < other.postal_code

address1 = MyAddress(1234, "Fuck St", "Stovner", "Oslo", "1234567")
address2 = MyAddress(5678, "Ninja St", "Nordstrand", "Bergen", "55443", 7)

print(address1)
print(address2)
print(address1.comesBefore(address2))