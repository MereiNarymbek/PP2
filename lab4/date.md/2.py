import datetime
today=datetime.datetime.now()
tomorow=today+datetime.timedelta(days=1)
yesterday=today-datetime.timedelta(days=1)
print(f"Today: {today}\nTomorow: {tomorow}\nYesterday: {yesterday}")
