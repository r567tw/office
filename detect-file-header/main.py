import chardet
import os

resource = "resource/"
for filename in os.listdir(resource):
    if filename is None or filename == '.gitkeep':
        continue
    filepath = os.path.join(resource,filename)
    rawdata=open(filepath,"rb").read()
    result = chardet.detect(rawdata)
    charenc = result['encoding']
    print("檔案 {} 編碼為 {}".format(filename,charenc))

