import datetime
import calendar

for i in range(1006, 2016, 10):
  date = datetime.datetime(i, 1, 26)
  if date.weekday() == 0 and calendar.isleap(i): print str(date.year), calendar.day_name[date.weekday()]
  # jan 26 1756, day before birth of mozart!
