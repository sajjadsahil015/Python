import time
import calendar
import datetime
print(time.time())

print(time.localtime(time.time()))
print(time.asctime(time.localtime(time.time())))

cal = calendar.month(2025,6)
print(cal)

print(datetime.datetime.now())
x= datetime.datetime.now()
print(x.strftime("%f")) 
print(x.strftime("%A"))
print(x.strftime("%Y"))
print(x.strftime("%B"))