from PIL import Image

img = Image.open('oxygen.png')

width = img.size[0]
height = img.size[1]

for i in range(0, width, 7):
    pix = img.getpixel((i, height/2))
    print(chr(pix[0]), end='')

print('')

binary = [105, 110, 116, 101, 103, 114, 105, 116, 121]
byte = bytearray(binary)

print(byte)
