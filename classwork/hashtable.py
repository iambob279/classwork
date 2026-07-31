MAXSIZE  = 20

hash_table_array = []
for i in range(MAXSIZE): # Creates fixed size array, empty at the start
    hash_table_array.append("")

def  make_hash(id): # sum ascii values, apply MOD 20
    hash_code = 0 
    for c in id:
        hash_code = hash_code + ord(c)
    return hash_code % 20

def menu():

    print("""
1. Enter a value
2. Show hash table
9. Quit""")

def main():
    opt = 0

    while True:
        menu()
        opt = int(input("Enter Choice: "))

        if opt == 1:
            id_input = input("Enter id: ")
            hash_index = make_hash(id_input)
            print ("Entering", id_input, "at", hash_index)
            hash_table_array[hash_index] = id_input
        elif opt == 2:
            for i in range(MAXSIZE):
                print (i, ' : ', hash_table_array[i])
        elif opt==9:
            break

main()
