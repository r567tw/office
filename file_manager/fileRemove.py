#將該資料夾的所有類似檔名的檔案複製挑出來
import os
import shutil

cur_path=os.path.dirname(__file__)
sample_tree=os.walk(cur_path)
output_dir = 'output'

target_dir = cur_path + '/' + output_dir

if not os.path.exists(target_dir):
    os.mkdir(target_dir)

for dirname,subdir,files in sample_tree:
    allfiles=[]
    basename = os.path.basename(dirname)

    if basename == output_dir:
        continue

    for file in files:
        ext=file.split('.')[-1]
        if ext=='jpg' or ext=='png' or ext=='JPG':
            allfiles.append(dirname+"\\"+file)
    
    if len(allfiles)>0:
        for imagefile in allfiles:
            filename = imagefile.split('\\')[-1]
            destfile = target_dir + '\\' + filename
            print(destfile)
            shutil.copy(imagefile, destfile)
print("完成......")
