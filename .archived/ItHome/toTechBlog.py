import requests
from bs4 import BeautifulSoup
import json


def getIthomeArticle(url):
    request = requests.get(sub_url)
    content = request.content
    soup = BeautifulSoup(content, "html.parser")
    data = soup.select_one(".qa-markdown")

    p_title = item.text.strip()
    p_status = "draft"
    p_content = data.decode_contents()
    p_categories = 44
    p_tags = [7, 4, 45]
    p_date = soup.select_one(".qa-header__info-time").text

    return {
        "title": p_title,
        "content": p_content,
        "status": p_status,
        "categories": p_categories,
        "tags": p_tags,
        "date": p_date,
    }


with open("data.json", "r") as reader:
    jf = json.loads(reader.read())

user_id = jf["id"]
user_passwd = jf["password"]
end_point_url_posts = jf["url"]

url = "https://ithelp.ithome.com.tw/users/20106999/ironman/2578"

request = requests.get(url)
content = request.content
soup = BeautifulSoup(content, "html.parser")

container = soup.select(".qa-list__title-link")

for item in container:
    if item:
        sub_url = item["href"].strip()
        payload = getIthomeArticle(sub_url)
        headers = {"content-type": "Application/json"}

        r = requests.post(
            end_point_url_posts,
            data=json.dumps(payload),
            headers=headers,
            auth=(user_id, user_passwd),
        )
        print(r.json()["id"])
        # break  # for test
