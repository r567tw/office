# importing the requests library
import requests
import json
import time

# defining the api-endpoint
URL = "https://official-joke-api.appspot.com/random_joke"
resultFile = "result.txt"

# data to be sent to api
# prepare = open("./requestData.json", "r")
# content = prepare.read()
# prepare.close()

headers = {"Content-Type": "application/json"}
# response = requests.post(url=URL, data=content, headers=headers)
# print(URL)
response = requests.get(url=URL, headers=headers, stream=True)
response.encoding = "utf-8"
# print(response)
result = json.loads(response.text)
f = open(resultFile, "w")
f.write(result["setup"])
f.close()

print("success")

