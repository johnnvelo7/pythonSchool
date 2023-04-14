class Employee:
    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary
#     __name and __salary = private
#  DO NOT use this way, just use single _ so anyone can know that

    def get_info(self):
        print(self.__name)
        print(self.__salary)

e1 = Employee("John", 999999)

e1.get_info()

print(e1._Employee__name)
print(e1._Employee__salary)

