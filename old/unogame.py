import random
cards = ()

def create_deck(cards):
    for i in range(1, 41):
        card = random.choice(["Yellow", "Red", "Green", "Yellow"])
        number = random.randint(0, 9)
        if len(card) or len(number) in cards == 10:
            card = random.choice(["Yellow", "Red", "Green", "Yellow"])
            number = random.randint(1, 9)
        elif card and number in cards:
            card = random.choice(["Yellow", "Red", "Green", "Yellow"])
            number = random.randint(1, 9)
        cards = (f"[{card}, {number}]")
    print(cards)
create_deck(cards)