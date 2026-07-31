#cuts lines from the text file
def filter(oldfile, newfile):
     infile = open(oldfile, "r")
     outfile = open(newfile, "w")
     while True:
         text = infile.readline()
         if len(text) == 0:
            break
         if text[0] == "W":
            continue

         # Put any more processing logic here
         outfile.write(text)

     infile.close()
     outfile.close()

filter("Tyger.txt", "NewTyger.txt")