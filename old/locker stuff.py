small = float(3.00)
medium = 6.50
large = float(10.00)
choice = 0
total = 0
lockers = 0

while True:
    days = int(input("How many days would you like to rent? = "))
    type = input("Input which locker type would you like = ").lower()
    while True:
        if type == "small":
            total = days * small
            break
        elif type == "medium":
            total = days * medium
            break
        elif type == "large":
            total = days * large
            break
        else:
            print("This is not a valid size, please try again")
            type = input("Input which locker type would you like = ").lower()

    weekly = input("Would you like to rent weekly for a 5% discount? = ").lower()
    while True:
        if weekly == "yes":
            total = total * 0.95
            break
        elif weekly == "no":
            break
        else:
            print("invalid input, try again")
            weekly = input("Would you like to rent weekly for a 5% discount? = ").lower()

    lockers = lockers + 1
    continue1 = input("Would you like to continue? = ").lower()
    if continue1 == "yes":
        print("-----------------------")
    elif continue1 == "no":
        print("Costs are being calculated.")
        print("-----------------------")
        break
    else:
        print("input not understood, continuting to cost calculation")
        print("-----------------------")
        break


print(f"Your total payment is £{total}")
print("----------")
print(f"The total ammounts of lockers being rented are {lockers}")

