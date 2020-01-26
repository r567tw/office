# 暫支援class id name
from selenium import webdriver
from time import sleep
import json

with open("auto.json", "r") as reader:
    jf = json.loads(reader.read())

data = jf["data"]
for i in range(0, len(data)):
    url = "https://tip.railway.gov.tw/tra-tip-web/tip/tip001/tip121/query"
    # 打開瀏覽器
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.get(url)
    browser.find_element_by_id("pid").send_keys("V121400894")
    browser.find_element_by_id("startStation").send_keys("1000-臺北")
    browser.find_element_by_id("endStation").send_keys("6000-臺東")
    # browser.find_element_by_id("rideDate").send_keys("2019/10/05")
    browser.find_element_by_id("trainNoList1").send_keys("72")
    browser.find_element_by_id("recaptcha-anchor-label").click()

    # form=data[i]['form']
    # for j in range(0,len(form)):
    #     element=form[j]["element"]
    #     if (element=='id'):
    #         browser.find_element_by_id(form[j]["key"]).send_keys(form[j]["value"])
    #     if (element=='class'):
    #         browser.find_element_by_class_name(form[j]["key"]).send_keys(form[j]["value"])
    #     if (element=='name'):
    #         browser.find_element_by_class_name(form[j]["key"]).send_keys(form[j]["value"])
    # #填完資料後要準備送出

    # submit=data[i]['submit']
    # element = submit["element"]
    # if (element=='id'):
    #     browser.find_element_by_id(submit["key"]).click()
    # if (element=='class'):
    #     browser.find_element_by_class_name(submit["key"]).click()
    # if (element=='name'):
    #     browser.find_element_by_class_name(submit["key"]).click()
