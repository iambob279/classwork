bags = int(input("How many bags - "))
sweets = int(input("How many sweets - "))
possible = 0

while bags == 0:
    possible = sweets - 3 
    bags = bags - 1

if possible == True:
    print("it is not possible")
else:
    print("It is possible")