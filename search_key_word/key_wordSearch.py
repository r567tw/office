import os,docx

cur_path=os.path.dirname(__file__)
sample_tree=os.walk(cur_path)

key_word = 'J'

for dirname,subdir,files in sample_tree:
    allfiles={}
    for file in files:
        ext=file.split('.')[-1]
        if ext=='txt' or ext=='docx':
            allfiles[dirname + "\\" + file]=ext
    
    if len(allfiles)>0:
        for file in allfiles:
            print("正在尋找 {} 檔案".format(file))
            try:
                if (allfiles[file]=='txt'):
                    #txt
                    fp= open(file,"r")
                    article = fp.readlines()
                    fp.close()
                    line=0
                    for row in article:
                        line += 1
                        if key_word in row:
                            print("在{}，第{}列找到{}".format(file,line,key_word))
                else:
                    #docx
                    doc = docx.Document(file)
                    line = 0
                    for p in doc.paragraphs:
                        line += 1
                        if key_word in p.text:
                            print("在第{}段文字找到{}\n{}".format(
                                line, key_word, p.text))
            except:
                print("{} 無法讀取".format(file))
print("完成......")
