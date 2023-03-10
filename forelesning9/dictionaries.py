contacts = {"Fred": 12340444, "John": 54321, "Mary": 56789, "Hadi": 1234455}

print(contacts)

for item in sorted(contacts):
    print(item, " = ", contacts[item])

for key, value in contacts.items():
    print(key, value)

