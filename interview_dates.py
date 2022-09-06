from datetime import datetime
import datetime
#today=datetime.datetime.now()
today=datetime.date(2022,9,11)


t1=today+datetime.timedelta(days=(7-today.weekday()))
t2=t1+datetime.timedelta(days=1)
t3=t2+datetime.timedelta(days=1)

print("dd/mm/yy")
print(t1.strftime("%d/%m/%y"))
print(t2.strftime("%d/%m/%y"))
print(t3.strftime("%d/%m/%y"))