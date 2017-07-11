from PIL import Image

img = Image.open("cave.jpg")
width = img.size[0]
height = img.size[1]
size = (width, height)
oddimg = Image.new("RGB", size)
evenimg = Image.new("RGB", size)
#print(img.getpixel(width/2, ))
for x in range(0, width):
    for y in range(0, height):
        if x % 2 == 1 and y % 2 == 1:
            oddimg.putpixel((x, y), img.getpixel((x, y)))
        elif x % 2 == 0 and y % 2 == 0:
            evenimg.putpixel((x, y), img.getpixel((x, y)))
oddimg.show()
evenimg.show()
