perkg = 10

weight = int(input("What is the weight of the luggage? = "))

def price(weight):
    if weight >= 50:
        print("Error: Your luggage is too heavy")
    elif weight >= 25:
        amount = weight - 25
        total = amount * perkg
        print(f"You must pay £{total} due to it being over 25 kg!")
    else:
        print("you do not have to pay extra for your luggage!")

price(weight)