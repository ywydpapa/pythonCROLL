from datetime import datetime,timedelta
import calendar

fromdate = datetime.today()
todate =  datetime.today() - timedelta(1)


print(fromdate.strftime("%Y%m%d"))
print(todate.strftime("%Y%m%d"))

last = calendar.monthrange(2022,2)

print (last[1])



