class Shape:
    def __init__(self,length):
        self.length = length
    def area(self):
        return 0
class Square(Shape):
    def area(self):
        return pow(self.length,2)

square = Square(3)
print(square.area())