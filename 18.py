import urllib, requests
from PIL import Image
import binascii
import cStringIO
import difflib
import gzip

response = requests.get("http://www.pythonchallenge.com/pc/return/deltas.gz",auth=("huge","file"))

file = cStringIO.StringIO(response.content)

with open("deltas.gz", "wb") as output:
  output.write(file.read())

with gzip.GzipFile("deltas.gz", "r") as input:
  lines = input.readlines()

sequence1 = []
sequence2 = []
for line in lines:
  sequence1.append(line[:55].strip() + '\n')
  sequence2.append(line[55:].strip() + '\n')

differ = difflib.Differ()
comparison = list(differ.compare(sequence1, sequence2))
with open("minusimg.png", "wb") as output:
  for each_result in comparison:
    if not each_result.startswith("-"): continue
    bytes = [ chr(int(b, 16)) for b in each_result[2:].split() ]
    for b in bytes:
      output.write(b)

with open("plusimg.png", "wb") as output:
  for each_result in comparison:
    if not each_result.startswith("+"): continue
    bytes = [ chr(int(b, 16)) for b in each_result[2:].split() ]
    for b in bytes:
      output.write(b)

with open("img.png", "wb") as output:
  for each_result in comparison:
    if not each_result.startswith(" "): continue
    bytes = [ chr(int(b, 16)) for b in each_result[2:].split() ]
    for b in bytes:
      output.write(b)

with open("img.png", 'rb') as input:
  im = Image.open(input)
  im.show()

with open("plusimg.png", 'rb') as input:
  im = Image.open(input)
  im.show()

with open("minusimg.png", 'rb') as input:
  im = Image.open(input)
  im.show()
