my_list = [1, 0, 6, 4, -9, 3, 8, 0]

print(max(my_list))
print(min(my_list))

my_list.sort()
print(my_list)

my_list.reverse()
print(my_list)

# DIFFERENT ADDRESS IN MEMORY

new_list = list(my_list)

print(my_list)
print(new_list)

print(id(my_list))
print(id(new_list))

my_list[0] = "AB"

print(id(my_list))
print(id(new_list))


#------------------------------------------------------------

print(my_list[2: 6])

# CREATE A LIST FROM ANOTHER LIST AND STORE IN OTHER MEMORY ADDRESS
new_list = my_list[:]

print(id(my_list))
print(id(new_list))

#  -----------------------------------------------------

friends = ["Harry", "Emily", "Bob"]
result = ""
for i in range(len(friends)):
    if i > 0:
        result = result + " ,"
    result = result + friends [i]

print(result)


#  ------------------------------------------------------

# n = my_list.index("a")
# n1 = my_list.index("a", n+1)
# print(n)
# print(n1)

my_list = ["a", "b", "c", "ddd", "9", "z", "a", "j", "a", "a"]

count = my_list.count("a")
if count > 0:
    n = my_list.index("a")
    print(n)

    for i in range(count -1):
        n = my_list.index("a", n+1)
        print(n)
else:
    print("'a' is not in the list")

#  -------------------------------------------------------------------

my_list = ["a", "b", "c", "ddd", "9", "z", "a", "j", "a", "a", "j", "j"]
duplicate = []

for item in my_list:
    if my_list.count(item) > 1:
        if item not in duplicate:
            duplicate.append(item)

print(my_list)
print(duplicate)

# ---------------------------------------------------

values = [1, 2, 3, 254, 4, 67, 88, 890]

LIMIT = 100
pos = 0
found = False

while pos < len(values) and not found:
    if values[pos] > LIMIT:
        found = True
    else:
        pos = pos + 1

if found:
    print("Value found at position: ", pos)
else: print("No element greater than 100")

#  ------------------------------------------------------

my_list = [1, 2, 3, 4, 4, 4, 5, 4, 8, 4, 4, 3]

# removing in lists is better with while loop

count = my_list.count(4)

for i in range(count):
        my_list.remove(4)
print(my_list)

#  ----------------------------------------------------

my_list = [1, 2, 3, 4, 4, 4, 5, 4, 8, 4, 4, 3]

i = 0
while i < len(my_list):
    if my_list[i] == 4:
        my_list.pop(i)
    else:
        i = i + 1

print(my_list)