from guizero import Text, App, PushButton

app = App("Quiz", layout="grid")
title = Text(app, text="Welcome to the quiz!", size=14, font="ComicSans", grid=[0,0])

points = 0 

def increment_points():
    global points 
    points += 1
    print(points)

def verify(fact):
    global points 
    if fact:
        print("Well done its right")
        increment_points()
        total.clear()
        total.append(f"points: {points}")
        app.update()
    else:
        print("That's wrong")

total = Text(app, text=f"points: {points}", size=14, font="ComicSans", grid=[1, 0])

title = Text(app, text="What is 2+2?", size=14, font="ComicSans", grid=[0, 1])
button_correct = PushButton(app, command=lambda: verify(True), text="4", grid=[0, 2])
button_incorrect = PushButton(app, command=lambda: verify(False), text="5", grid=[1,2 ])

title = Text(app, text="What is 5+5?", size=14, font="ComicSans", grid = [0,3])
button_correct = PushButton(app, command=lambda: verify(True), text="10", grid=[0, 4]) 
button_incorrect = PushButton(app, command=lambda: verify(False), text="12", grid=[1, 4])

title = Text(app, text="What is 50 - 10?", size=14, font="ComicSans", grid=[0, 5])
button_correct = PushButton(app, command=lambda: verify(False), text="35", grid=[0,6]) 
button_incorrect = PushButton(app, command=lambda: verify(True), text="40", grid=[1, 6])

title = Text(app, text="What is 4 + 9?", size=14, font="ComicSans", grid=[0, 7])
button_correct = PushButton(app, command=lambda: verify(True), text="13", grid=[0, 8]) 
button_incorrect = PushButton(app, command=lambda: verify(False), text="14", grid=[1, 8])

title = Text(app, text="What is 10+5?", size=14, font="ComicSans", grid=[0, 9])
button_correct = PushButton(app, command=lambda: verify(True), text="15", grid=[0, 10]) 
button_incorrect = PushButton(app, command=lambda: verify(False), text="13", grid=[1, 10])

app.display()
