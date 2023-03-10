import random
# TASK 2

values = []
for i in range(10):
    values.append(random.randint(1,100))
# TASK 3A

for value in values:
    print(value, end=" ")
print()

# TASK 3B
sum_values = 0
for value in values:
    sum_values += value
print("Sum of all elements in this list:", sum_values)

# TASK 3C
count_even = 0
for value in values:
    if value % 2 == 0:
        count_even += 1
print("Number of even elements in the list:", count_even)


count_even = [num for num in values if num % 2 == 0]
print("List with even numbers only:", count_even)

