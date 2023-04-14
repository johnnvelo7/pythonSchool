class Animal:
    def __init__(self, age):
        self.age = age
        self.name = None
        # none is an object that does not have any value
        # It has two attributes in this example

    def get_age(self):
        return self.age
        # This is a method to return the age or the current object

    def set_name(self, name=""):
        self.name = name
        # name="" is just setting it to be empty string

    def get_name(self):
        return self.name

    def set_age(self, new_age):
        self.age = new_age
        # setting new value for age

    def __str__(self):
        return "Animal: " + self.name + " --> " + str(self.age)

print("Animal Class Test")
a1 = Animal(5)
print(a1.age)
# public attributes can be directly accessed

print(a1.get_age())
a1.set_name("Sike")
print(a1.get_name())
print(a1)
# a1 is an object created from Animal Class
