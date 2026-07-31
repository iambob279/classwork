import random
import time
turn = True
lost = False
dlost = False
amount = 0
dealer = 0
while turn == True:
    if amount > 22:
        print("You lost")
        lost = True
        break
    print("-----------------------------------------")
    print(f"You: {amount}\nDealer: {dealer}")
    option = int(input("1. Hit\n2. Stand\n"))
    if option == 1:
        card = random.randint(1, 11)
        if card <= 10:
            amount = amount + card
        if card == 10:
            card = random.choice(["King", "Queen", "Jack"])
        if card == 11:
            card = "Ace"
            if amount > 10:
                amount = amount + 1
            elif amount < 10:
                amount = amount + 11
        print(f"You drew a {card} card!")
    
    if option == 2:
        turn = False
        
turn = True
if lost == False:
    print("Dealers turn")
    while turn == True:
        for i in range(1, 4):
            print("----------------------------------")
            print(f"You: {amount}\nDealer: {dealer}")
            card = random.randint(1, 11)
            if card <= 10:
                dealer = dealer + card
            if card == 10:
                card = random.choice(["King", "Queen", "Jack"])
            if card == 11:
                card = "Ace"
                if dealer > 10:
                    dealer = dealer + 11
                elif dealer < 10:
                    dealer = dealer + 1
            print(f"Dealer drew a {card}")
            time.sleep(3)
            
            if dealer > 21:
                dlost = True
                print("player won")
        turn = False
            
    if dlost == False:
        if dealer > amount:
            print("Dealer won")
        else:
            print("Player won")