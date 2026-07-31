exit = False
exit2 = False
while exit == False:
    choice = int(input("What do you want to do?\n1. write to a file\n2. read a file\n3. exit\n"))
    if choice == 1:
        filename = input("What is the name of the file?\n")
        file = open(filename, "w")
        print("Please write what you want to write, write 'exit' to leave\n")
        while exit2 == False:
            text = input("")
            if text == "exit":
                file.close()
                exit2 == True
            else:
                file.write(f"{text}\n")




while True:
    choice = int(input("What do you want to do?\n1. write to a file\n2. read a file\n3. exit\n"))

    if choice == 1:
        filename = input("What is the name of the file?\n")
        with open(filename, "w") as file:  # Using a context manager to automatically close the file
            print("Please write what you want to write, write 'exit' to leave\n")
            while True:
                text = input("")
                if text == "exit":
                    break  # Exit the inner loop
                else:
                    file.write(f"{text}\n")

    elif choice == 2:
        # Add code for reading a file here
        pass

    elif choice == 3:
        break  # Exit the outer loop

    else:
        print("Invalid choice. Please try again.")