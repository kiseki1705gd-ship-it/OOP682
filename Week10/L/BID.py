class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

class Spquare(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
    def set_width(self, width):
        self.height = width
        self.width = width
    def set_height(self, height):
        self.height = height
        self.width = height
def resize_rectangle(rectangle, new_width, new_height):
    rectangle.set_width(new_width)
    rectangle.set_height(new_height)
    return rectangle.width * rectangle.height

rect = Rectangle(2, 3)
print("Rectangle area:", resize_rectangle(rect, 4, 5))
sq = Spquare(4)
print("Square area:", resize_rectangle(sq, 4, 5))

