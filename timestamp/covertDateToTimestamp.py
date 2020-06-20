import datetime

date_string = input("請輸入要轉換的日期(格式:%Y/%m/%d):")
date = datetime.datetime.strptime(date_string, "%Y/%m/%d")
timestamp = date.timestamp()
# print(timestamp)
print("{}".format(int(timestamp)))