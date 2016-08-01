'''
import email.feedparser
with open("19.txt", "r") as input:
  content = input.read()

differ = email.FeedParser()

parser.feed(content)
print parser.close() 
#python 19.py | aplay
#SORRY!
'''
import email
import mimetypes
import wave
import StringIO
from optparse import OptionParser

with open("19.txt", "r") as input:
  msg = email.message_from_file(input)
  
  for file in msg.walk():
    if file.get_content_maintype() != 'multipart':
      data = file.get_payload(decode=True)
      wave1 = wave.open(StringIO.StringIO(data))
      wave2 = wave.open("indian.wav", "w")
      wave2.setnchannels(wave1.getnchannels())
      wave2.setsampwidth(wave1.getsampwidth())
      wave2.setframerate(wave1.getframerate())
      wave2.big_endian = 1
      wave2.writeframes(wave1.readframes(wave1.getnframes()))
      wave1.close()
      wave2.close()
      
