from StringIO import StringIO
from zipfile import ZipFile
from urllib import urlopen
import re

url = urlopen("http://www.pythonchallenge.com/pc/def/channel.zip")
zipfile = ZipFile(StringIO(url.read()))
next = 90052

comments = []

while True:
  cfile = zipfile.open(str(next) + ".txt")
  z_str = cfile.read()
  comments.append(zipfile.getinfo(str(next) + ".txt").comment)
  print z_str
  match = re.match('.*?([0-9]+)$', z_str)
  if match == None:
    break  
  next = int(match.group(1))
  print next

print ''.join(comments)
