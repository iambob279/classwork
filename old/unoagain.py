import random
cardss = []

for i in range(1,4):
    cards = random.choice(["Red", "Green", "Blue", "Yellow"])
    number = str(random.randint(1, 9))
    if cards and number in cardss:
        cards = random.choice(["Red", "Green", "Blue", "Yellow"])
        number = str(random.randint(1, 9))
    cardss.append([cards, number])

print(cardss)