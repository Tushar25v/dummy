class Shape:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return 0

class Rectangle(Shape):
    def area(self):
        return self.width * self.height


rectangle_instance = Rectangle(width=5, height=10)


print("Area of the rectangle:", rectangle_instance.area())
