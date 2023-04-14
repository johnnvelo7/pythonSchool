class Address:
    def __init__(self, house_number, street, city, state, postal_code, apartment_number=None):
        self.house_number = house_number
        self.street = street
        self.apartment_number = apartment_number
        self.city = city
        self.state = state
        self.postal_code = postal_code

    def __str__(self):
        address = f"{self.house_number} {self.street}"
        if self.apartment_number:
            address += f", Apt #{self.apartment_number}"
        address += f"\n{self.city}, {self.state} {self.postal_code}"
        return address

    def comes_before(self, other):
        return self.postal_code < other.postal_code

address1 = Address(1234, "Main St", "Anytown", "CA", "12345")
address2 = Address(5678, "Maple Ave", "Mytown", "NY", "67890", 9)

print(address1)
# Output:
# 1234 Main St
# Anytown, CA 12345

print(address2)
# Output:
# 5678 Maple Ave, Apt #9
# Mytown, NY 67890

print(address1.comes_before(address2))
# Output: True
