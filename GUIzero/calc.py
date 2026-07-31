from guizero import App, Text, Box, PushButton
number = ""
number2 = ""
shown = ""
push = False
add = False
minus = False
div = False
times = False

def pushed():
    global push
    print("Pushing complete")
    push = True

def one(num):
    global number
    global number2
    global push
    global shown
    if push == True:
        number2 = number2 + str(num)
        shown = number2
    else:
        number = number + str(num)
        shown = number
    inputed.clear()
    inputed.append(f"numbers: {shown}")
    app.update()

def adding():
    global add
    global push
    global shown
    print("Adding done")
    add = True
    push = True
    shown = shown + "+"
    inputed.clear()
    inputed.append(f"numbers: {shown}")
    app.update()

def sub():
    global minus
    global push
    global shown
    print("subbing done")
    minus = True
    push = True
    shown = shown + "-"
    inputed.clear()
    inputed.append(f"numbers: {shown}")
    app.update()

def multiply():
    global times
    global push
    global shown
    print("multiply done")
    times = True
    push = True
    shown = shown + "*"
    inputed.clear()
    inputed.append(f"numbers: {shown}")
    app.update()

def divide():
    global div
    global push
    global shown
    print("divide done")
    div = True
    push = True
    shown = shown + "/"
    inputed.clear()
    inputed.append(f"numbers: {shown}")
    app.update()

def calcu():
    global number
    global number2
    global shown
    if add:
        result = int(number) + int(number2)
    elif minus:
        result = int(number) - int(number2)
    elif div:
        result = int(number) / int(number2)
        result = round(result, 4)
    elif times:
        result = int(number) * int(number2)
    shown = result
    inputed.clear()
    inputed.append(f"numbers: {shown}")
    app.update()

def clear():
    global shown
    global number
    global number2
    global push
    global minus
    global add
    number = ""
    number2 = ""
    shown = ""
    push = False
    add = False
    minus = False
    inputed.clear()
    inputed.append(f"numbers: {shown}")
    app.update()
    print("Clear complete")

app = App(layout="grid")

inputed = Text(app, text=f"numbers: {shown}", grid=[1,0])

button = PushButton(app, args=[1], command=one, text="1", grid=[0,1])
button = PushButton(app, args=[2], command=one, text="2", grid=[1,1])
button = PushButton(app, args=[3], command=one, text="3", grid=[2,1])
button = PushButton(app, args=[4], command=one, text="4", grid=[0,2])
button = PushButton(app, args=[5], command=one, text="5", grid=[1,2])
button = PushButton(app, args=[6], command=one, text="6", grid=[2,2])
button = PushButton(app, args=[7], command=one, text="7", grid=[0,3])
button = PushButton(app, args=[8], command=one, text="8", grid=[1,3])
button = PushButton(app, args=[9], command=one, text="9", grid=[2,3])
button = PushButton(app, args=[0], command=one, text="0", grid=[1,4])

button = PushButton(app, command=adding, text="+", grid=[3,1])
button = PushButton(app, command=sub, text="-", grid=[3,2])
button = PushButton(app, command=multiply, text="*", grid=[3,3])
button = PushButton(app, command=divide, text="/", grid=[3,4])
button = PushButton(app, command=clear, text="clear", grid=[3,5])
button = PushButton(app, command=calcu, text="=", grid=[2,4])

app.display()