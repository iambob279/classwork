import sqlite3
Continue = True


connection = sqlite3.connect('MyFilms.db')
cursor = connection.cursor()

while Continue == True:
    title = input("Enter title: ")
    yearReleased = input ("Enter Year released: ")
    rating = input ("Enter Rating: ")
    duration = int(input("Enter duration: "))
    genre = input("Enter genre: ")

    # Find the biggest id so far and add 1 to it - only fetches one row
    cursor.execute("select max(filmID) from tblFilms")
    row = cursor.fetchone() #just gets one row
    ID = (row[0])+1

    #cursor = connection.cursor()
    cursor.execute ("INSERT INTO tblFilms VALUES (?,?,?,?,?,?)", [ID, title, yearReleased, rating, duration, genre])
    connection.commit()            
    Continue = input("Would you like to add another record? = ").lower
    if Continue == "yes":
        Continue = True
    else:
        Continue = False

connection.close()

    