import smtplib
import cv2
from email.mime.image import MIMEImage

try:
    smtp_gmail = smtplib.SMTP("smtp.gmail.com", 587)
    smtp_gmail.ehlo()
    smtp_gmail.starttls()
    smtp_gmail.login("logicsolutionjimmy", "qwert231")
except:
    print("connect ERROR")
    exit()

from_addr = "logicsolutionjimmy@gmail.com"
to_addr = "r567tw@gmail.com"
# message = "Subject:FirstTest\nHello World"
img = cv2.imread("car.jpg")
img_encode = cv2.imencode(".jpg", img)[1]  # 將 img 編碼為 jpg 格式，[1]返回資料, [0]返回是否成功
img_bytes = img_encode.tobytes()
message = MIMEImage(img_bytes)
message["Content-type"] = "application/octet-stream"
message["Content-Disposition"] = 'attachment; filename="handsome.jpg"'
message["Subject"] = "測試的主旨"
message["From"] = "粉絲"
message["To"] = "偉大的站長"
# message["Cc"] = "副本"

status = smtp_gmail.sendmail(from_addr, to_addr, message.as_string())

if not status:
    print("Success")
else:
    print("Fail")
    print(status)
smtp_gmail.quit()
