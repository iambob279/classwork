correct = 0
ans = int(input("What is Unicode?\n1. A character set\n2. A programming language\n3. A website?\n------\n"))
if ans == 1:
    print("Correct!")
    correct = correct + 1
else:
    print("Wrong, it was 1")

ans = int(input("What is the letter 'a' in ASCII?\n1. 01001001\n2. 01100001\n3. 01000001\n------\n"))
if ans == 2:
    print("Correct!")
    correct = correct + 1
else:
    print("Wrong, it was 2")

ans = int(input("What is the letter 'B' in ASCII?\n1. 01000010\n2. 01110011\n3. 01100110\n------\n"))
if ans == 1:
    print("Correct!")
    correct = correct + 1
else:
    print("Wrong, it was 1")

ans = int(input("What is the letter 'z' in ASCII?\n1. 01001001\n2. 01111010\n3. 00100001\n------\n"))
if ans == 2:
    print("Correct!")
    correct = correct + 1
else:
    print("Wrong, it was 2")

ans = int(input("What is the letter 'D' in ASCII?\n1. 01111000\n2. 01111100\n3. 01000100\n------\n"))
if ans == 3:
    print("Correct!")
    correct = correct + 1
else:
    print("Wrong, it was 3")

ans = int(input("What is the letter 'f' in ASCII?\n1. 01000110\n2. 01100110\n3. 01000001\n------\n"))
if ans == 2:
    print("Correct!")
    correct = correct + 1
else:
    print("Wrong, it was 2")

ans = int(input("What is the letter ' ' in ASCII?\n1. 00100000\n2. 00111010\n3. 01111011\n------\n"))
if ans == 1:
    print("Correct!")
    correct = correct + 1
else:
    print("Wrong, it was 1")

print(f"You finished the quiz, you got {correct}/7 correct.")