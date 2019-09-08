import cv2  # 匯入 cv2 套件
import requests
import re

img = cv2.imread("car.jpg")
img_encode = cv2.imencode(".jpg", img)[1]  # 將 img 編碼為 jpg 格式，[1]返回資料, [0]返回是否成功
img_bytes = img_encode.tobytes()

key = "b23eb43836e346a2bdc14c81c26a14d7"
url = "https://westcentralus.api.cognitive.microsoft.com/vision/v2.0/recognizeText?mode=Printed"
header = {"Ocp-Apim-Subscription-Key": key, "Content-Type": "application/octet-stream"}

recognize = requests.post(url, headers=header, data=img_bytes)
if recognize.status_code != 202:  # 202 代表接受請求
    print(recognize.json())
    print("請求失敗")
    exit()

result_url = recognize.headers["Operation-Location"]
result = requests.get(result_url, headers={"Ocp-Apim-Subscription-Key": key})

carcard = ""  # 紀錄車牌
print(result.json())
lines = result.json()["recognitionResult"]["lines"]
for i in range(len(lines)):
    text = lines[i]["text"]  # 取得辨識文字
    m = re.match(r"^[\w]{2,4}[-. ][\w]{2,4}$", text)  # 匹配是否為車牌格式
    if m != None:  # 匹配成功
        carcard = m.group()
        print(carcard)

