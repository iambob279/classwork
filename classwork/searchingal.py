num = 0
index = -1
def binarysearch(mylist, item):
  result = 0
  Tlength = len(mylist)
  length = Tlength / 2
  length = int(length)
  while result != item:
    print(length)
    result = mylist[length]
    if result > item:
        length = (range(result - 1, Tlength)) / 2
        result = length
    elif result < item:
        length = (range(-1, result)) / 2
        result = length
  return result

def linearsearch(mylist, item, num, index):
  result = 0
  while result != item:
    result = mylist[num]
    num = num + 1
    index = index + 1
  return index

mylist = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
#Ask user for item to search for
item = int(input("Enter number to search for: "))
#Code to call binary search and print index of item found
print("Item found at index:", binarysearch(mylist, item), linearsearch(mylist, item, num, index))
#Code to call linear search and print index of item found
#print("Item found at index:", linearsearch(mylist,item))

