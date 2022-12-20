from math import pi


class Circle():
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        area = self.length * self.width
        return area

    def circumfarence(self):
        w = self.width * 2
        l = self.length *2
        circumfarence = l + w

circle = Circle(100,200)
print("area " + circle.area())        


