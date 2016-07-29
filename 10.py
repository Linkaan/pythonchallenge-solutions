start = "1"

def look_and_say(start):
  looking_at = start[0]
  count = 0
  next_item = ''
  
  for item in start:
    if item == looking_at:
      count += 1
    else:
      next_item += str(count) + looking_at
      count = 1
    
    looking_at = item
  next_item += str(count) + looking_at
  
  return next_item

for i in range(30):
  start = look_and_say(start)

print(len(start))
