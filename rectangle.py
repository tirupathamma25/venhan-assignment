class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width
        
    def area(self):
        print("area: {}".format(self.length * self.width))
        
    def perimeter(self):
        print("perimeter: {}".format((self.length + self.width) * 2))
       
        
r = Rectangle(23.3,18.8)
r.area()
r.perimeter()
 