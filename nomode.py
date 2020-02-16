from PIL import Image
file = input("Filename: ")
img1 = Image.open(file)
img2 = Image.open('hl2menu.png')
width1, height1 = img1.size
width2, height2 = img2.size
k = [1, width1 / 1280, width1 / 1920]
for i in k:
    img1 = Image.open(file)
    y_offset = int((height1 - height2) / 2)
    x_offset = int(width1 / 50)
    img2 = img2.resize((int(width2 * i), int(height2 * i)))
    img1.paste(img2.convert('RGBA'), (x_offset, y_offset), img2.convert('RGBA'))
    img1.save(str(i)+file)
