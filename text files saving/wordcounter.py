f = open("quotes.txt")
content = f.read()
f.close()

words = content.split()
num_words = len(words)
print(f"There are {num_words} words in the file.")