import random
total = 0
count = 0

picks = ()

while count == 3:
    while count == 3:
        cards = random.choice(["Red", "Green", "Blue", "Yellow"])
        number = random.randint(1, 9)
        if cards and number in picks:
            cards = random.choice(["Red", "Green", "Blue", "Yellow"])
            number = random.randint(1, 9)
        picks = picks + (f"{cards}", number)
    count = count + 1

print(picks)
total = picks[1] + picks[3] + picks[5]
print(f"the chosen cards are:\n{picks[0]} with number {picks[1]}\n{picks[2]} with number {picks[3]}\n{picks[4]} with number {picks[5]}")
print(f"The total sum is {total}")



