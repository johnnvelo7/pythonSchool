import random

# Generate the list of values
values = []
for i in range(10):
    values.append(random.randint(1, 100))

# Separate the even and odd numbers into two different lists
even_values = []
odd_values = []
for value in values:
    if value % 2 == 0:
        even_values.append(value)
    else:
        odd_values.append(value)

# Print the original list and the even/odd lists
print("Original list:", values)
print("Even values:", even_values)
print("Odd values:", odd_values)
