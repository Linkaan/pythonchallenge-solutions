import re

if __name__ == '__main__':
  s = ''.join([line.rstrip() for line in open('equality.txt')])    
  pattern = re.compile('[a-z][A-Z]{3}[a-z][A-Z]{3}[a-z]', re.MULTILINE)
  matches = pattern.findall(s, re.MULTILINE)
  print matches
