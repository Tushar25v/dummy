class Shape:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return 0

class Rectangle(Shape):
    def area(self):
        return self.width * self.height

class Triangle(Shape):
    def area(self):
        return 0.5 * self.width * self.height


rectangle_instance = Rectangle(width=8, height=4)
triangle_instance = Triangle(width=6, height=9)


print("Area of the rectangle:", rectangle_instance.area())  
print("Area of the triangle:", triangle_instance.area())    
