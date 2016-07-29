from PIL import Image
import operator
import urllib, cStringIO

def get_pink_position(image, rown):
  for i in range(640):
    if image.getpixel((i+0, rown)) == (255,0,255) and \
       image.getpixel((i+1, rown)) == (255,0,255) and \
       image.getpixel((i+2, rown)) == (255,0,255) and \
       image.getpixel((i+3, rown)) == (255,0,255) and \
       image.getpixel((i+4, rown)) == (255,0,255):
      return i+2

file = cStringIO.StringIO(urllib.urlopen("http://www.pythonchallenge.com/pc/return/mozart.gif").read())
im = Image.open(file)

rgb_im = im.convert('RGB')
width, height = im.size

image = Image.new('RGB', (640, 480))
pix = image.load()

for y in range(480):
  offset = 0 - get_pink_position(rgb_im, y)
  print "correcting offset %d, row %d" % (offset, y)
  if offset != 0:
    for i in range(640):      
      pix[i, y] = rgb_im.getpixel(((i-offset) % 640, y))
  else:
    for i in range(640):
      pix[i, y] = rgb_im.getpixel(((i+offset), y))

image.show()
image.save("mozart.png") #romance
