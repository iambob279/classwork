from guizero import App, Text, PushButton, Window, TextBox
import sqlite3

conn = sqlite3.connect("MyFilms.db")
cursor = conn.cursor()

def show_search():
    search_window.show(wait=True)

def show_add():
    add_window.show(wait=True)

def show_delete():
    delete_window.show(wait=True)

def Search():
    userinput = field.value
    print(userinput)
    for row in cursor.execute(f'SELECT * FROM tblFilms WHERE title = "{userinput}"'):
        print(row)
        displayed.clear()
        displayed.append(row)
        app.update

def Add():
    title = field2.value
    yearReleased = field3.value
    rating = field4.value
    duration = field5.value
    genre = field6.value
    
    cursor.execute("select max(filmID) from tblFilms")
    row = cursor.fetchone() #just gets one row
    ID = int(row[0])+1
    ID = str(0 + ID)

    cursor.execute("INSERT INTO tblFilms VALUES (?,?,?,?,?,?)", [ID, title, yearReleased, rating, duration, genre])
    conn.commit()
    app.info("Adding", "Data added successfully")

def Delete():
    filmID = field_filmID.value
    print(filmID)
    for row in cursor.execute(f'SELECT title FROM tblFilms WHERE filmID = "{filmID}"'):
        print(row)
        name = row
    if app.yesno("Deletion request", f"Are you sure you want to delete '{name}'?"):
        cursor.execute(f"DELETE FROM tblFilms WHERE filmID = {filmID}")
        conn.commit()
        app.info("Deletion completed", f"'{name}' has been deleted!")
    else:
        app.error("Cancelling deletion", f"'{name}' will no longer be deleted")

def quit():
    conn.close()
    app.hide()

def userquit():
    search_window.hide()
    add_window.hide()
    delete_window.hide()

app = App("Film adder")
app.bg = "#FFFFFF"

#window set up
search_window = Window(app, title="Search")
add_window= Window(app, title="Add")
delete_window= Window(app, title="Delete")
search_window.hide()
add_window.hide()
delete_window.hide()

#main window
text = Text(app, text="Welcome, what would you like to do?")
button = PushButton(app, show_search, text="Search", align="top")
button = PushButton(app, show_add, text="Add", align="top")
button = PushButton(app, show_delete, text="Delete", align="top")
button = PushButton(app, quit, text="Quit", align="top")

#search window
text = Text(search_window, text="Welcome to the search menu")
field= TextBox(search_window, text="Enter film name")
search = PushButton(search_window, Search, text="Search")
displayed = Text(search_window, text="Information")
close = PushButton(search_window, userquit, text="Close")

#add window
text = Text(add_window, text="Welcome to the add menu")
field2 = TextBox(add_window, text="title")
field3 = TextBox(add_window, text="yearReleased")
field4 = TextBox(add_window, text="rating")
field5 = TextBox(add_window, text="duration")
field6 = TextBox(add_window, text="genre")
add = PushButton(add_window, Add, text="Add to database")
close = PushButton(add_window, userquit, text="Close")

#delete window
text = Text(delete_window, text="Welcome to the delete menu")
field_filmID= TextBox(delete_window, text="Enter film ID")
search = PushButton(delete_window, Delete, text="Search")
close = PushButton(delete_window, userquit, text="Close")

app.display()