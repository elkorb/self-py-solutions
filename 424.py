import datetime
import calendar

date_string = input("Enter a date:").strip()
date = datetime.datetime.strptime(date_string, '%d/%m/%Y')
print(calendar.day_name[calendar.weekday(date.year, date.month, date.day)])