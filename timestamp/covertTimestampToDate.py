import datetime from datetime

dateTimestamp = input("請輸入timestamp:")
dateString = datetime.fromtimestamp(dateTimestamp)
print(dateString)
# date = datetime.datetime.strptime(date_string, "%Y/%m/%d")
# print("{}".format(int(timestamp)))