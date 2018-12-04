"""
Define a class named Shape and its subclass Square.
The Square class has an init function which takes a length as argument.
Both classes have a area function which can print the area of the shape where Shape's area is 0 by default.

It might be used like this:
square = Square(3)
print(square.area())
"""


class Shape:
    def __init__(self, length):
        self.length = length

    def area(self):
        return 0


class Square(Shape):
    def area(self):
        return pow(self.length, 2)


first = Square(3)
print(first.area())
second = Square(33)
print(second.area())
third = Shape(10)
print(third.area())
