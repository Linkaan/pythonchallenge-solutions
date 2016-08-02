import urllib2, base64, requests
from PIL import Image, ImageDraw
from StringIO import StringIO

request = urllib2.Request("http://www.pythonchallenge.com/pc/hex/white.gif", None, headers = {"Authorization": "Basic %s" % base64.b64encode(b"butter:fly").decode()})
response = urllib2.urlopen(request)
frame = Image.open(StringIO(response.read()))
#im.show()

width, height = frame.size
image = Image.new('RGB', (width, height), (0,0,0))
pix = image.load()

draw = ImageDraw.Draw(image)

sequence = [4]

tx = 0
ty = 100
nframes = 0
while frame:
  rgb_im = frame.convert('RGB')
  for y in range(height):
    for x in range(width):
      if rgb_im.getpixel((x, y)) != (0, 0, 0):
        pix[x,y] = (255, 255, 255)
        #print "frameno %i at (%s): %s" % (nframes, (x, y), rgb_im.getpixel((x, y)))
        new_y = ((y - 98) / 2)-1
        new_x = ((x - 98) / 2)-1
        print "x: %i, y: %i (%i)" % (new_x, new_y, new_x + new_y*3)
        if new_y == 0 and new_x == 0:
          tx += 25
          ty = 100
        tx += new_x
        ty += new_y
        draw.point([tx, ty])
        '''
        if sequence[-1] != new_x + new_y*3:
          draw.line(((width / 3) * (sequence[-1] % 3), (height / 3) * (sequence[-1] / 3), (width / 3) * new_x, (height / 3) * new_y), fill=(255, 0, 0), width=3)
          sequence.append(new_x + new_y*3)
        '''
  nframes += 1
  try:
    frame.seek( nframes )
  except EOFError:
    break

print sequence

image.save("white.gif")
image.show()
