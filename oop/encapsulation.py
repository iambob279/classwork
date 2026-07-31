import math

class Circle:
    #attributes
    radius=0.0
    circumference=0.0

    def __init__ (self, given_radius):
        self.radius = given_radius
        self.circumference = self.radius*2*math.pi

    def get_radius (self):
        return self.radius

    def set_radius (self, given_radius):
        self.radius = given_radius
        self.circumference = self.radius*2*math.pi

    def get_circumference(self):
        return self.circumference


def main():

    my_circle = Circle(5)
    print ("Circumference = ", my_circle.get_circumference(), "radius = ", my_circle.get_radius())

    my_circle.set_radius (4)
    print ("Circumference = ", my_circle.get_circumference(), "radius = ", my_circle.get_radius())

    my_circle.radius=10
    print ("Circumference = ", my_circle.get_circumference(), "radius = ", my_circle.get_radius())

main()