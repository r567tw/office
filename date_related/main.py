from datetime import datetime


for j in range(28):
    d = j+1
    print(d,end=':')
    count = 0
    for i in range(12):
        m = i+1
        date=datetime.date(datetime(year=2022, month=m, day=d))
        if date.isoweekday() in [1, 2, 3, 4, 5]:
            count+=1
    print(count)
        
