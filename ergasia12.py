from datetime import datetime, time
import calendar
import datetime

def date_diff_in_seconds(dt2, dt1):
  timedelta = dt2 - dt1
  return timedelta.days * 24 * 3600 + timedelta.seconds

def dhms_from_seconds(seconds):
	minutes, seconds = divmod(seconds, 60)
	hours, minutes = divmod(minutes, 60)
	days, hours = divmod(hours, 24)
	return (days, hours, seconds)

#Specified date
year=int(input('Enter a year: '))
month=int(input('Enter a month: '))
day=int(input('Enter a day: '))
date1 = datetime.datetime(year, month, day)

#Current date
date2 = datetime.datetime.now()

print("\n%d days/%d hours/%d seconds" % dhms_from_seconds(date_diff_in_seconds(date2, date1)))

print('The Monthrange is: ' , calendar.monthrange(year,month))








# import datetime
# d0 = datetime.datetime.now()
# date1 = datetime.datetime(int(input('Enter a year: ')), int(input('Enter a month: ')), int(input('Enter a day: ')))
# print()
# delta = d0 - date1

