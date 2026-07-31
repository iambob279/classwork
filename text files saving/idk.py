f = open("smiley.png", "rb")
g = open("newsmiley.png", "wb")

while True:
    buf = f.read(1024)
    if len(buf) == 0:
         break
    g.write(buf)

f.close()
g.close()