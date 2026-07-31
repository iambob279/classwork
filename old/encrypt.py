letters = []
complete = ""
myword = input("input the word = ").upper()

for i in myword:
    letter = ord(i)
    letters.append(letter)

print(letters)

def convert(letters, complete):
    for i in letters:
        i = i + 13
        if i > 90:
            i = i - 26
        char = chr(i)
        complete = complete + char
    
    print(complete)


convert(letters, complete)


#letter = letter + 13
#print(chr(letter))