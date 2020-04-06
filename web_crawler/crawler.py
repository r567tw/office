import requests
from bs4 import BeautifulSoup
import json

with open("data.json", "r") as reader:
    jf = json.loads(reader.read())

data = jf["data"][0]
url = data["url"]

request = requests.get(url)
content = request.content
soup = BeautifulSoup(content, "html.parser")

container = soup.select(data["select"])

# 接下來只是寫入result.txt檔案的事情
file = open("result.txt", "w",encoding='utf8')
for item in container:
    if item:
        value = item.get_text().strip()
        print(value)
        # break # for test
        file.write("{}\n".format(value))  # 檔案寫入
file.close()
