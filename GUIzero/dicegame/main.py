from guizero import App, PushButton, Text, Picture
import random



def button_pushed():
  print("Button was pushed")

def dice():
  dice1 = random.choice(["dice1.png", "dice2.png", "dice3.png", "dice4.png", "dice5.png", "dice6.png"])
  print (dice1)
  dicee = Picture(app, image=dice1)

app = App("Dice")
app.bg = "#CCCCCC"
dice_text = Text(app, text="5 5")
dice_text.text_size = 24
dice_text.font = "Courier New"

button = PushButton(app, dice, text= "Roll Dice")
dice()

app.display()