from guizero import App, PushButton, Slider, Text
from time import ctime

def update_date():
    the_date.value = ctime(date_slider.value)

def are_you_sure():
    if app.yesno("Confirmation", "Are you sure?"):
        app.info("Thanks", "Button pressed")
    else:
        app.error("Ok", "Cancelling")

def flash_text():
    if title.visible:
        title.hide()
    else:
        title.show()

app = App("A bad mix of everything")

title = Text(app, text="Welcome!", size="14", font="ComicSans", color="green")
app.repeat(1000, flash_text)

the_date = Text(app)
date_slider = Slider(app, start=0, end=999999999, command=update_date)

button = PushButton(app, command=are_you_sure)
app.info("Application started", "Well done you started the application")
app.display()