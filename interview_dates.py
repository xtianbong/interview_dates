from datetime import datetime
import datetime
today=datetime.datetime.now()
#today=datetime.date(2022,9,11) #test case


t1=today+datetime.timedelta(days=(7-today.weekday())+7) #starts from the monday after the next
t2=t1+datetime.timedelta(days=1)
t3=t2+datetime.timedelta(days=1)

print("dd/mm/yy   hh:mm")
print(t1.strftime("%d/%m/%y")+"0900 to 1900")
print(t2.strftime("%d/%m/%y")+"0900 to 1900")
print(t3.strftime("%d/%m/%y")+"0900 to 1900")