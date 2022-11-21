from PIL import Image, ImageDraw, ImageFont, ImageColor
import sys

'''
from PIL import Image
from urllib.request import urlopen
url = "https://www.utcsheffield.org.uk/olp/assets/sites/3/2021/07/UTC-Sheffield-Olympic-Legacy-Park-Horizontal.png"
img = Image.open(urlopen(url))

reduction = 5

(width, height) = (img.width // reduction, img.height // reduction)
img1 = img.resize((width, height))


dat1 = img1.getdata()
print("Image data is ", len(dat1)*3,"bytes long")
#print("img",list(dat1)[:100])

img2 = img1.quantize()
dat2 = img2.getdata()
print("Indexed image data is", len(img2.getpalette()), "bytes for pallete and " , len(dat2), "bytes for image")
print(len(img2.getpalette())/3)

'''

def run_length_encoding(seq):
  compressed = []
  count = 1
  char = seq[0]
  for i in range(1,len(seq)):
    if seq[i] == char and count<256:
      count = count + 1
    else :
      compressed.append([char,count])
      char = seq[i]
      count = 1
  compressed.append([char,count])
  return compressed

text = "Hello World"

print(text, len(text))

text2 = run_length_encoding(text)

print(text2, len(text2)*2)

'''
dat3 = run_length_encoding(dat2)

print("RLE encoded image data is", len(img2.getpalette()), "bytes for pallete and " , len(dat3)*2, "bytes for image")
print(dat3)

#print(img2.getpixel((20,0)))

img2.show()
'''