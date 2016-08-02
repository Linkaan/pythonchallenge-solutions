import urllib2, base64, requests
import mmap
import zlib
import bz2
import os
from StringIO import StringIO
from zipfile import ZipFile

request = urllib2.Request("http://www.pythonchallenge.com/pc/hex/unreal.jpg", None, headers = {"Authorization": "Basic %s" % base64.b64encode(b"butter:fly").decode(), "Range": "bytes=1152983631-"})
response = urllib2.urlopen(request)
fp = StringIO(response.read())
with ZipFile(fp, "r") as z:
  with open("package_0.pack", 'wb') as f:
    f.write(z.read("package.pack", pwd="invader"[::-1]))

next_package = 0
compression_type = "zlib"

log = open("package_log.txt", "w")

while True:
  print "inflating file %s (%s compressed data)" % (next_package, compression_type)
  if compression_type == "bzip2":
    log.write(" ")
    with bz2.BZ2File("package_%i.pack" % (next_package)) as zipfile:
      str_object1 = zipfile.read()
      next_package += 1
      with open("package_%i.pack" % (next_package), 'wb') as output:
        output.write(str_object1)
  elif compression_type == "zlib":
    log.write("#")
    with open("package_%i.pack" % (next_package), 'rb') as input:
      str_object1 = input.read()
      str_object2 = zlib.decompress(str_object1)
    next_package += 1
    with open("package_%i.pack" % (next_package), 'wb') as output:
      output.write(str_object2)
  else:
    print "can't inflate file package_%i.pack (unknown compression type)" % (next_package)
  with os.popen("file package_%i.pack" % (next_package)) as f:
    is_pack = f.read()
    if "zlib compressed data" in is_pack or "TeX font metric data" in is_pack or "BS image" in is_pack:
      compression_type = "zlib"
    elif "bzip2 compressed data" in is_pack:
      compression_type = "bzip2"
    elif ".pack: data" in is_pack:
      print "Reversing file and trying again"
      log.write("\n")
      with open("package_%i.pack" % (next_package),"rb") as input:
        input.seek(0, 2)  # Seek relative to end of file
        size = input.tell()
        inputfd = input.fileno()
        mm = mmap.mmap(inputfd, size, mmap.MAP_PRIVATE, mmap.PROT_READ)
        next_package += 1
        compression_type = "unknown"
        with open("package_%i.pack" % (next_package),"wb") as output:
          for i in range(len(mm),0,-1):
            if i == 1:
              output.write(mm[0:1])
            else:
              output.write(mm[i-1:i-2:-1])
      with os.popen("file package_%i.pack" % (next_package)) as f2:
        is_pack = f2.read()
        if "zlib compressed data" in is_pack or "TeX font metric data" in is_pack or "BS image" in is_pack:
          compression_type = "zlib"
        elif "bzip2 compressed data" in is_pack:
          compression_type = "bzip2"
        else:
          print "package_%i.pack is different!!" % (next_package)
          break
    else:
      print "package_%i.pack is different!!" % (next_package)
      break

log.close()

with open("package_%i.pack" % (next_package)) as input:
  content = input.read()
  print "%s (%s)" % (content,content[::-1])

with open("package_log.txt") as input:
  print input.read()
