gfx = open("evil2.gfx", "rb")

images = {}

for i in range(5):
  images[i] = open("evil_image" + str(i) + ".jpg", "wb")

bytes = gfx.read()
for i in range(0, len(bytes), 5):
  for j in range(5):
    images[j].write(bytes[i + j])


disproportionality
