from pprint import pprint
from PIL import Image
import operator
import urllib, cStringIO

file = cStringIO.StringIO(urllib.urlopen("http://www.pythonchallenge.com/pc/def/oxygen.png").read())
im = Image.open(file)

d = {}

rgb_im = im.convert('RGB')
width, height = im.size
new_str = ""
last_c = None
for x in range(width):
  for y in range(height):
    r, g, b = rgb_im.getpixel((x, y))
    try:
      d[(r, g, b)] += 1
      value = d[(r, g, b)]
      if value == 63:
        #if r >= ord('a') and r <= ord('z'):
        if not last_c == r:
          last_c = r
          new_str += chr(r)
    except KeyError:
      d[(r, g, b)] = 1

print new_str
#pprint(sorted_d)


