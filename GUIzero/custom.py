from guizero import App, Text, Picture

app = App("cat")
app.bg = "#F2A2C3"

title_text = Text(app, text="No way is that a cat???")
title_text.text_size = 20
title_text.font = "Helvetica"

cat = Picture(app, image="cat.png")

apply_text = Text(app, text="So cool frfr")
apply_text.text_size = 14

title_text = Text(app, text="Another one???")
title_text.text_size = 20
title_text.font = "Arial"

cat2 = Picture(app, image="cat2.png")

apply_text = Text(app, text="This is crazy")
apply_text.text_size = 14
apply_text.font = "Comic sans"

app.display()