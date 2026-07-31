import math

class Shape: # base class that defines common features
    #attributes
    area=0.0

    def get_area (self):
        return self.area

    def set_area (self, given_area):
        self.area = given_area

class Circle(Shape): #inherits from Shape, can use its methods
    #attributes
    radius = 0.0

    def __init__(self, given_radius):
        self.radius = given_radius
        self.set_area (math.pi*self.radius*self.radius)

class Rectangle(Shape): #inherits from Shape, can use its methods
    #attributes
    length = 0.0
    width = 0.0

    def __init__ (self, given_length, given_width):
        self.length=given_length
        self.width=given_width
        self.set_area  (self.length*self.width)

class triangle(Shape):
    length = 0
    height = 0
    def __init__(self, given_length, given_height):
        self.length = given_length
        self.height = given_height
        self.set_area ((self.height * self.length) / 2)


def main():

    c1 = Circle(5)
    r1 = Rectangle(2, 4)
    t1 = triangle(2, 5)

    print ("area of c1 is", c1.get_area()) #inherits from Shape, can use its methods

    print ("area of r1 is", r1.get_area ())

    print(f"area of t1 is {t1.get_area()}")


        
main()