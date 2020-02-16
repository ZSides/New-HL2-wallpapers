from PIL import Image
file = input("Filename: ")
mode = int(input("Mode [1, 2 or 3]: "))
img1 = Image.open(file)
img2 = Image.open('hl2menu.png')
width1, height1 = img1.size
width2, height2 = img2.size
y_offset = int((height1 - height2) / 2)
x_offset = int(width1 / 50)
if mode == 1:
    k = width1 / 1280
elif mode == 2:
    k = width1 / 1920
else:
    k = 1
img2 = img2.resize((int(width2 * k), int(height2 * k)))
img1.paste(img2.convert('RGBA'), (x_offset, y_offset), img2.convert('RGBA'))
img1.save("hl2-"+file)
