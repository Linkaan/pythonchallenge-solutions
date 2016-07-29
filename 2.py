str = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
new_str = ""
for i in range(len(str)):
  cc = ord(str[i])
  if cc < ord('a') or cc > ord('z'):
    new_str += str[i]
    continue
  new_cc = ord('a') + (cc - ord('a') + 2) % 26
  new_str += chr(new_cc)
print new_str
