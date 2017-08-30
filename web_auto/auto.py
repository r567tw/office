#暫支援class id name
from selenium import webdriver
from time import sleep
import json

with open('auto.json', 'r') as reader:
    jf = json.loads(reader.read())

data=jf['data']
for i in range(0,len(data)):
    url=data[i]['url']
    #打開瀏覽器
    browser=webdriver.Chrome()
    browser.maximize_window()
    browser.get(url)   
    form=data[i]['form']
    for j in range(0,len(form)):
        element=form[j]["element"]
        if (element=='id'):
            browser.find_element_by_id(form[j]["key"]).send_keys(form[j]["value"])
        if (element=='class'):
            browser.find_element_by_class_name(form[j]["key"]).send_keys(form[j]["value"])
        if (element=='name'):
            browser.find_element_by_class_name(form[j]["key"]).send_keys(form[j]["value"])
    #填完資料後要準備送出

    submit=data[i]['submit']
    element = submit["element"]
    if (element=='id'):
        browser.find_element_by_id(submit["key"]).click()
    if (element=='class'):
        browser.find_element_by_class_name(submit["key"]).click()
    if (element=='name'):
        browser.find_element_by_class_name(submit["key"]).click()
