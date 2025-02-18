import datetime
date_format="%Y-%m-%d %H:%M:%S"
date1=datetime.datetime.strptime(input(),date_format)
date2=datetime.datetime.strptime(input(),date_format)
difference=date1-date2
print(difference.seconds)