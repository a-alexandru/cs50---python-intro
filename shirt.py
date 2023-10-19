from PIL import Image, ImageOps


im = Image.open("before1.jpg")
img = ImageOps.fit(im, (600, 600))
shirt = Image.open("shirt.png")
Image.Image.paste(img, shirt)

img.show()
