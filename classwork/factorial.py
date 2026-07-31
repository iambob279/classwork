list = []
userinput = int(input("Enter a number = "))

def factorial(userinput):
    number = 1
    while userinput != 0:
        list.append(userinput)
        userinput -= 1

    for i in list:
        number = number * i
    print(number)

factorial(userinput)