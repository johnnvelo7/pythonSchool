my_list = [1, 2.3, "a", True]

new_list = my_list

print(my_list)
print(new_list)

print(id(new_list))
print(id(my_list))

my_list[0] = "A"

print(my_list)
print(new_list)

# LIST REFERS TO SAME POSITION IN MEMORY


print(my_list[-3])