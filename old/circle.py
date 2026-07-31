diameter = 0
circumference = 0
radius = 0
area = 0

diameter = int(input("what is the diameter of the circle? = "))

def circle_area(diameter, radius, area):
    radius = diameter / 2
    area = 3.14 * (radius * radius)
    print(f"the area is {area}")

circle_area(diameter, radius, area)

def circle_circumference(diameter, circumference):
    circumference = diameter * 3.14
    print(f"The circumference is {circumference}")

circle_circumference(diameter, circumference)

