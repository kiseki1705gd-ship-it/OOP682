
from abc import abstractmethod
class Shape:
    @abstractmethod
    def reszize(self, new_width, new_height): pass
    @abstractmethod
    def area(self): pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def reszize(self, new_width, new_height):
        self.width = new_width
        self.height = new_height
    def area(self):
        return self.width * self.height
class Spquare(Shape):
    def __init__(self, side):
        self.side = side
    def reszize(self, new_width, new_height):
        self.side = new_width
    def area(self):
        return self.side * self.side
def resize(shape, new_width, new_height):
    shape.reszize(new_width, new_height)
    return shape.area()
rect = Rectangle(2, 3)
print("Rectangle area:", resize(rect, 4, 5))
sq = Spquare(3)
resize(sq, 4, 5)