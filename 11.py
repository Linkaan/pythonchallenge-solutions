from PIL import Image

im = Image.open("cave.jpg")
rgb_im = im.convert('RGB')
pix = rgb_im.load()
width, height = rgb_im.size

image = Image.new('RGB', (width / 2, height / 2))
image_pix = image.load()

for x in range(0, width, 2):
  for y in range(0, height, 2):
    if x+1 > width or y+1 > height: continue
    value = rgb_im.getpixel((x, y))
    print value
    image_pix[x/2, y/2] = value

image.save("oddeven2.png", "PNG")
