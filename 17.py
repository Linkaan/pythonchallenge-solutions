import requests
import urllib
import bz2
import xmlrpclib

print requests.get("http://www.pythonchallenge.com/pc/def/linkedlist.php").cookies["info"]

cookies = []

next = 12345
while True:
  response = urllib2.urlopen("http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing=" + str(next))
  html = response.read()
  print html
  print requests.get("http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing=" + str(next)).cookies
  cookies.append(requests.get("http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing=" + str(next)).cookies["info"])
  if not "and the next busynothing is" in html:
    break
  next = int(html.split()[-1])

print cookies

'''
cookies = ['B', 'Z', 'h', '9', '1', 'A', 'Y', '%26', 'S', 'Y', '%94', '%3A', '%E2', 'I', '%00', '%00', '%21', '%19', '%80', 'P', '%81', '%11', '%00', '%AF', 'g', '%9E', '%A0', '+', '%00', 'h', 'E', '%3D', 'M', '%B5', '%23', '%D0', '%D4', '%D1', '%E2', '%8D', '%06', '%A9', '%FA', '%26', 'S', '%D4', '%D3', '%21', '%A1', '%EA', 'i', '7', 'h', '%9B', '%9A', '%2B', '%BF', '%60', '%22', '%C5', 'W', 'X', '%E1', '%AD', 'L', '%80', '%E8', 'V', '%3C', '%C6', '%A8', '%DB', 'H', '%26', '3', '2', '%18', '%A8', 'x', '%01', '%08', '%21', '%8D', 'S', '%0B', '%C8', '%AF', '%96', 'K', 'O', '%CA', '2', '%B0', '%F1', '%BD', '%1D', 'u', '%A0', '%86', '%05', '%92', 's', '%B0', '%92', '%C4', 'B', 'c', '%F1', 'w', '%24', 'S', '%85', '%09', '%09', 'C', '%AE', '%24', '%90']
'''

string = ''.join(cookies)

string2 = urllib.unquote_plus(string)

with open("cookies.data", 'wb') as output:
 for c in string2:
  output.write(c) # hmm, this looks like bzip...

decompressed = bz2.decompress(string2) # call Leopold

proxy = xmlrpclib.ServerProxy("http://www.pythonchallenge.com/pc/phonebook.php")
print proxy.phone("Leopold") # 555-VIOLIN

cookie = {"info": 'the flowers are on their way'}
response = requests.get("http://www.pythonchallenge.com/pc/stuff/violin.php",cookies=cookie)
print response.text # balloons.html

