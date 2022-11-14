from PIL import Image, ImageDraw, ImageFont, ImageColor
import sys



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

dat3 = run_length_encoding(dat2)

print("RLE encoded image data is", len(img2.getpalette()), "bytes for pallete and " , len(dat3)*2, "bytes for image")


'''
Image.getpalette(rawmode='RGB')

Image.tobytes(encoder_name='raw')


Image.resize(size, resample=None, box=None, reducing_gap=None)
 # Provide the target width and height of the image
    


def run_length_encoding(seq):
  compressed = []
  count = 1
  char = seq[0]
  for i in range(1,len(seq)):
    if seq[i] == char:
      count = count + 1
    else :
      compressed.append([char,count])
      char = seq[i]
      count = 1
  compressed.append([char,count])
  return compressed
 
seq = 'AACCCBBBBBAAAAFFFFFFFF'
list1 = run_length_encoding(seq)
 
compressed_seq = ''
 
for i in range(0,len(list1)):
  for j in list1[i]:
    compressed_seq += str(j)
 
print(compressed_seq)

def run_length_decoding(compressed_seq):
  seq = ''
  for i in range(0,len(compressedcompressed_seq = ''
 
for i in range(0,len(list1)):
  for j in list1[i]:
    compressed_seq += str(j)
 
print(compressed_seq)_seq)):
    if compressed_seq[i].isalpha() == True:
      for j in range(int(compressed_seq[i+1])):
        seq += compressed_seq[i]
 
  return(seq)


from adafruit_bitmapsaver import save_pixels
.
.
.
save_pixels('/sd/pypaint.bmp', self._fg_bitmap, self._fg_palette)




# TODO : Compression
# TODO : Demonstrate Colour Indexing
# TODO : Demonstrate Run Length Encoding
# TODO : Decompress


pallet = [
    "#FFFFFF",
    "#000",
    "pink",
    (0,255,0)
]

# create an image
out = Image.new("RGB", (150, 100), pallet[0])
d = ImageDraw.Draw(out)

d.rectangle([0,10,20,30], fill=pallet[3])
'''

print(img2.getpixel((20,0)))
#img2.show()