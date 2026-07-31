import random
num = 0

list = []

for i in range(0,10):
    num = random.randint(1,49) 
    while num in list:
        num = random.randint(1,49) 
    list.append(num)

print(list)