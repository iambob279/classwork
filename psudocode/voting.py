Acount = 0
Bcount = 0
Ccount = 0
vote = ""

while vote == "END":
    vote = input("Who do you vote for?").lower()
    if vote == "a":
        Acount += 1
    elif vote == "b":
        Bcount += 1
    elif vote == "c":
        Ccount += 1
    else:
        print("No canidate vote found")
print(f"A = {Acount}\nB = {Bcount}\nC = {Ccount}")