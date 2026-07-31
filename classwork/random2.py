#procedure to set up local variable 
def add_first(num1):
    #declare global variable num2
    global num2
    num2 = 10
    print("add_first:", num1, num2, num1 + num2)

#procedure to add two variables and display result
def add_second(num1):
    global num2
    print("add_second:", num1, num2, num1 + num2)

num1 = 0
add_first(num1)
add_second(30)
print("main:", num1, num2, num1 + num2)
