class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"< {str(self.x)}, {str(self.y)} >"

    def __add__(self, other):
        first = self.x + other.x
        second = self.y + other.y
        return Coordinate(first, second)
#     first refers to the first coordinate, second refers to the second coordinate

    def distance(self, other):
        x_diff_sq = (self.x - other.x) ** 2
        y_diff_sq = (self.y - other.y) ** 2

        return (x_diff_sq + y_diff_sq) ** 0.5

c1 = Coordinate(2,3)
c2 = Coordinate(5,9)

print(c2)
print(c1 + c2)
print(c2.distance(c1))