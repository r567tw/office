import json


file_path = raw_input("please input your whole file path:")
fo = open(file_path, "r")
content = fo.read() 
fo.close()
parsed = json.loads(content)
print(json.dumps(parsed, indent=4, sort_keys=True))