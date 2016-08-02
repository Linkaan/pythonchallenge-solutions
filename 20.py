import urllib, requests
import urllib2, base64
from zipfile import ZipFile

response = requests.get("http://www.pythonchallenge.com/pc/hex/unreal.jpg",auth=("butter","fly"), headers={'Range': 'bytes=%i-' % (30203)})
print response.headers
print response.text
print
end_range = int(response.headers["content-range"].split("-")[1].split("/")[0])
total_range = int(response.headers["content-range"].split("-")[1].split("/")[1])

while end_range < total_range and response.ok:
  response = requests.get("http://www.pythonchallenge.com/pc/hex/unreal.jpg",auth=("butter","fly"), headers={'Range': 'bytes=%i-' % (end_range + 1)})
  print response.headers
  print response.text
  print
  if response.ok:
    end_range = int(response.headers["content-range"].split("-")[1].split("/")[0])
  else:
    break

response = requests.get("http://www.pythonchallenge.com/pc/hex/unreal.jpg",auth=("butter","fly"), headers={'Range': 'bytes=%i-' % (total_range + 1)})
print response.headers
print response.text
print
start_range = int(response.headers["content-range"].split("-")[0].split(" ")[1])

while True:
  response = requests.get("http://www.pythonchallenge.com/pc/hex/unreal.jpg",auth=("butter","fly"), headers={'Range': 'bytes=%i-' % (start_range - 1)})
  print response.headers
  print response.text
  print
  if response.ok:
    start_range = int(response.headers["content-range"].split("-")[0].split(" ")[1])
  else:
    break

request = urllib2.Request("http://www.pythonchallenge.com/pc/hex/unreal.jpg", None, headers = {"Authorization": "Basic %s" % base64.b64encode(b"butter:fly").decode(), "Range": "bytes=1152983631-"})
response = urllib2.urlopen(request)

with open("data20.zip", "wb") as output:
    output.write(response.read())

with ZipFile("data20.zip") as input:
    input.extractall(pwd="invader"[::-1])
