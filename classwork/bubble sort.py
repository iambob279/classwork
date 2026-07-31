list = [64, 34, 25, 12, 22, 11, 90, 5]
sort = []
swap = False
length = len(list)
lengsorted = 0

while swap == True:
    for i in range(0, length - 2):
        if list[0] < list[1]:
            sort.append(list[1])
        else:
            print("done")
    swap = True

print(sort)

#wrong