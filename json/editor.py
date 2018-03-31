import json

def replace(filename,search,replace):
    f = open(filename, "r+")
    content = f.read() 
    position = content.find(search) 
    f.seek(position,0) 
    f.write(replace) 
    f.close()

def print_json(filename):
    fo = open(filename, "r")
    content = fo.read() 
    fo.close()
    parsed = json.loads(content)
    print(json.dumps(parsed, indent=4, sort_keys=True))
    fo.close()


file_path = raw_input("please input your whole file path:")
print_json(file_path)
c_search = raw_input("please input your string want to be replaced: ")
c_replace = raw_input("please input your string want to replace: ")
replace(file_path,c_search,c_replace)
print_json(file_path)