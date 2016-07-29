import pickle
import urllib2

urls = urllib2.urlopen("http://www.pythonchallenge.com/pc/def/banner.p")
deser = pickle.load(urls)
for cols in deser:
  r_str = ""
  for rows in cols:
    for i in range(rows[1]):
      r_str += rows[0]
  print r_str
