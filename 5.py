import urllib2
import re

next = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=8022'
while True:
  response = urllib2.urlopen(next)
  html = response.read()
  pattern = re.compile('\d+', re.MULTILINE)
  matches = pattern.findall(html, re.MULTILINE)
  if len(matches) > 0:
    next = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=" + str(int(matches[0]) / 2)
    print int(matches[0]) / 2
  else:
    break
