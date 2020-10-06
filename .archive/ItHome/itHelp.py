import requests
from bs4 import BeautifulSoup

url = "https://ithelp.ithome.com.tw/users/20106999/collections/ironman"

request = requests.get(url)
content = request.content

soup = BeautifulSoup(content, "html.parser")

container = soup.select(".pagination > li")
pages = [1]
# https://ithelp.ithome.com.tw/users/20106999/collections/ironman?page=3
logs = open("content.txt", "w+", encoding="utf8")
number = 0
# for page in pages:
# if page:
url = "https://ithelp.ithome.com.tw/users/20106999/collections/ironman?page=1"
# print(url);
request = requests.get(url)
content = request.content

soup = BeautifulSoup(content, "html.parser")

titles = soup.select(".qa-list__title--ironman")
# print(titles)
for title in titles:
    number += 1
    logs.write("- [ ]{}.{}\n".format(number, title.get_text().strip()))
    # print(title.get_text().strip())
    # value = item.get_text()
    # print(value)
    # break #這裡也提一個起手式的遺珠之憾，就是你可以用continue和break來處理 迴圈敘述，這裏為了我之前debug方便，使用break來讓我先只看一個的結果。
logs.close()
