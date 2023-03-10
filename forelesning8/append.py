my_list = [1, 2.3, "a", True, "a"]

my_list.append("Python")

print(my_list)

my_list.append(-2.6)

print(my_list)

my_list.insert(1, "PGR107")

print(my_list)

if "Python" in my_list:
    print("Nice")

n = my_list.index("a")
n1 = my_list.index("a", n+1)
print(n)
print(n1)