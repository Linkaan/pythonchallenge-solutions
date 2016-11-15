from string import maketrans

text = "va gur snpr bs jung?"
trans = maketrans("abcdefghijklmnopqrstuvwxyz", "nopqrstuvwxyzabcdefghijklm")
print(text.translate(trans))

# import this includes "in the face of" "ambigiouty"
