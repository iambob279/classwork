img = 0
imga = int(input("What is the actual image size in micrometers? = "))
img = int(input("What is the image size in centimetres? = "))

def magnifications(imga, img):
    magnification = (img * 10000) / imga
    magnification = round(magnification, 2)
    print(f"The magnification is {magnification}X")

magnifications(img, imga)