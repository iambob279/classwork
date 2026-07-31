length = 0
width = 0
height = 0
vol = 0
gallons = 0

length = int(input("What is the length? = "))
width = int(input("What is the width? = "))
height = int(input("What is the height? = "))

def volume(vol,length,width,height):
    vol = length * width * height
    print(f"The litre amount is {vol}")

volume(vol,length,width,height)

def litres_to_gallons(vol, gallons, length, width, height):
    vol = length * width * height
    gallons = vol / 4.546
    print(f"The gallons amount is {gallons}")

litres_to_gallons(vol, gallons, length, width, height)