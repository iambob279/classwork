from guizero import App, Text, Picture

app = App("Computer Science")
app.bg = "#FBFBD0"

title_text = Text(app, text="Study Computer Science A level")
title_text.text_size = 20
title_text.font = "Helvetica"

cat = Picture(app, image="computing.png")

apply_text = Text(app, text = "Apply at CANDI now")
apply_text.text_size = 14

app.display()