import os
import hashlib
import shutil
import imghdr
#定義scan 的資料夾、結果的資料夾、可接受的圖片副檔名

scan_dir='./image'
output_dir = 'output'
img_array=['jpg','JPG','png','jpef','gif']

sample_tree=os.walk(scan_dir)
cur_path=os.path.dirname(__file__)

allfiles=[]
allmd5s=dict()
n=0


target_dir = cur_path + '/' + output_dir
if not os.path.exists(target_dir):
    os.mkdir(target_dir)

for dirname,subdir,files in sample_tree:
    basename = os.path.basename(dirname)
    #print(files)
    if basename == output_dir:
        continue
    for file in files:
        ext=file.split('.')[-1]
        #print(file)
        if (ext in img_array):
            allfiles.append(basename+'/'+file)

if len(allfiles)>0:
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

print("完成......結果在output 資料夾")
