class Shape:
    def __init__(self,length,width):
        self.length = length
        self.width = width
        
    def area(self):
        print("area: {}".format(self.length * self.width))
        
    def perimeter(self):
        print("perimeter: {}".format((self.length + self.width) * 2))
       
        
class Circle(Shape):
    PI = 3.142
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        print("area: {}".format(Circle.PI * self.radius * self.radius))
       
    def perimeter(self):
        print("perimeter: {}".format(2 * Circle.PI * self.radius))

        
class Rectangle(Shape):
    def area(self):
        super().area()
    def perimeter(self):
        super().perimeter()
        
c = Circle(20)
c.area()
c.perimeter()
r = Rectangle(20,15)
r.area()
r.perimeter()