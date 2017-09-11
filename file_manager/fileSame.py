import os
import hashlib
import shutil

cur_path=os.path.dirname(__file__)
sample_tree=os.walk(cur_path)
output_dir = 'output'
allmd5s=dict()
n=0


for dirname,subdir,files in sample_tree:
    allfiles=[]
    basename = os.path.basename(dirname)

    if basename == output_dir:
        continue

    for file in files:
        ext=file.split('.')[-1]
        if ext=='jpg' or ext=='png':
            allfiles.append(dirname+"/"+file)
    
    if len(allfiles)>0:
        target_dir = dirname + '/' + output_dir
        if not os.path.exists(target_dir):
            os.mkdir(target_dir)
        counter = 0
        for imagefile in allfiles:
            img_md5 = hashlib.md5(open(imagefile,'rb').read()).digest()
            if img_md5 in allmd5s:
                print("找到下列重複的檔案")
                print(os.path.abspath(imagefile))
                print(allmd5s[img_md5]+"\n")
                os.remove(imagefile) #刪除檔案
            else:
                filename = imagefile.split('.')[0]
                m_filename = "p" + str(counter)
                destfile = target_dir + '/' + m_filename + '.jpg'
                print(destfile)
                shutil.copy(imagefile, destfile)
                counter += 1
                allmd5s[img_md5] = os.path.abspath(imagefile)
print("完成......")
