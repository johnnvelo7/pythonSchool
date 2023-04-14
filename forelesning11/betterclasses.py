class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
# self.name and self.age = attributes
# name and self is for the parameter
# Does not have to be name "self" can be something else

# __init__() is a method

    def introduce(self):
        print(f"My name is {self.name} and I am {self.age} years old.")
p1 = Person("John", 24)
print(p1.name, p1.age)

# There is a print function inside already
p1.introduce()

p2 = Person("John", 30)
p2.introduce()
# Self is always the first parameter in init
p1.name = "Bill"
p1.introduce()

# p1 and p2 are accessing the Person Class because it is public


