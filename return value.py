#return value
from cmath import pi


def circle_area(radius):
    area = radius * pi
    return area

radius = input("enter radius: ")
radius= int(radius)
print(circle_area(radius))