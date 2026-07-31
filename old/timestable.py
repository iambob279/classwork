user = 0
times = 1
num = 0

while True:
    try:
        user = int(input("What number would you like the timestable for? = "))
        while user > 10:
            print("this is not allowed")
            user = int(input("What number would you like the timestable for? = "))
        while user < 0:
            print("This is not allowed, try again")
            user = int(input("What number would you like the timestable for? = "))
    
        for i in range(0, 11):
            num = user * times
            times = times + 1
            print(num)
            if times == 11:
                break
    except:
        print("Not a number")