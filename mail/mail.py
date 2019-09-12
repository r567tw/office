import smtplib
from email.mime.text import MIMEText
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
message = MIMEText("Hello我是小小君", "plain", "utf-8")
message["Subject"] = "測試的主旨"
message["From"] = "粉絲"
message["To"] = "偉大的站長"
message["Cc"] = "副本"

status = smtp_gmail.sendmail(from_addr, to_addr, message.as_string())

if not status:
    print("Success")
else:
    print("Fail")
    print(status)
smtp_gmail.quit()
