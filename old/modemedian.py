numbers = []
numbers1 = 0
total = 0
count = 0
avg = 0
end = False
import statistics #allows to easily get the mode, median and range in a given list
try:
    while end != True:
        numbers1 = int(input("What numbers would you like to enter? = "))
        total = total + numbers1
        count = count + 1
        numbers.append(numbers1)
except:
    print(numbers)

avg = total / count
avg = round(avg,3)
print(f"The average is {avg}")
print(f"The mode is {statistics.mode(numbers)}")
print(f"The median ia {statistics.median(numbers)}")
