num = 0
num2 = 0
user = 0
times = 3
#this does not work

results = []
while True:
    try:
        num = int(input("Input a number = "))
        for i in range(0,8):
            if times == num:
                times = times + 1
            else:
                num2 = (num % times)
                results.append(num2)
                times = times + 1     

        print(results)

        if 0 in results:
            print("This is a prime number")
            results = []
        else:
            print("this is not a prime number")
            results = []

    except:
        print("this is not a number")