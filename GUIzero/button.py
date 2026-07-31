from guizero import App, PushButton

def button_pushed():
  print("Button was pushed")
  
app = App("Say Hello")
app.bg = "#FBFBD0"

button = PushButton(app, button_pushed, text= "Push me")

app.display()
