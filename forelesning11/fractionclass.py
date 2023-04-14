class Fraction:
    def __init__(self, numerator, denomenator):
        self.numerator = numerator
        self.demonenator = denomenator

    def __str__(self):
        return str(self.numerator) + "/" + str(self.demonenator)

    def __add__(self, other):
        top = self.numerator * other.demonenator + self.demonenator * other.numerator
        bottom = self.demonenator * other.demonenator

        return Fraction(top, bottom)

    def __sub__(self, other):
        top = self.numerator * other.demonenator + self.demonenator * other.numerator
        bottom = self.demonenator * other.demonenator
        return Fraction(top, bottom)

    def __float__(self):
        return self.numerator / self.demonenator

    def inverse(self):
        return Fraction(self.demonenator, self.numerator)

a = Fraction(2,3)
b = Fraction(4,6)

print(a)
print(b)

c = a + b
d = a -b
print(c)
print(d)
print(22/15)

print("%.2f" % float(c))

print(b.inverse())