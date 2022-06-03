#get current date and time

from datetime import datetime
now=datetime.now()
print("current date and time=",now)

dt=now.strftime("%d/%m%/%Y %H:%M:%S")
print("date and time=",dt)
