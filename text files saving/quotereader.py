import random
continue1 = False
def run():
    file = open("quotes.txt", "r")
    number = random.randint(0, 82)
    for i in range(1, number):
        i = file.readline()
        line = i
    print(line)

while continue1 != True:
    run()
    choice = input("Would you like another?\n").lower()
    if choice == "yes":
        print("---------------------------------------")
    else:
        continue1 == False
        break
