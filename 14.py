from PIL import Image
import operator
import urllib, cStringIO

file = cStringIO.StringIO(urllib.urlopen("http://www.pythonchallenge.com/pc/return/wire.png").read())
im = Image.open(file)

rgb_im = im.convert('RGB')
width, height = im.size

image = Image.new('RGB', (100, 100))
pix = image.load()

j = 100
t = 0
r_y = 0
r_x = 0
for k in range(50):
  for i in range(4):
    if i == 0:
      for x in range(j):    
        value = rgb_im.getpixel((t + x, 0))
        print r_x + x, r_y
        pix[r_x + x, r_y] = value
      r_x += j-1
      r_y += 1
      t += j      
      j -= 1
    if i == 1:
      for x in range(j):    
        value = rgb_im.getpixel((t + x, 0))
        print r_x, r_y + x
        pix[r_x, r_y + x] = value
      r_y += j-1
      r_x -= 1
      t += j
    if i == 2:
      for x in range(j):    
        value = rgb_im.getpixel((t + x, 0))
        print r_x - x, r_y
        pix[r_x - x, r_y] = value
      r_x -= j-1
      r_y -= 1
      t += j      
      j -= 1
    if i == 3:
      for x in range(j):    
        value = rgb_im.getpixel((t + x, 0))
        print r_x, r_y - x
        pix[r_x, r_y - x] = value    
      r_y -= j-1
      r_x += 1
      t += j  

image.show()
image.save("wire3.png")
