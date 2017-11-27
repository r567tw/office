import csv
import os
import sys
import shutil

# 先填寫database 的csv 檔名、scan 的資料夾名稱、target_dir 的資料夾名稱
# 註: 資料夾名稱需加註'/',如果是要目前檔案所在目錄的話則就'./'
# 若要資料完整保留不改名的話則就在csv 檔裡面保持原名
# python run 即可
database	='data.csv'
scan_dir	='./'
target_dir	='result/'

resultfile		=target_dir+'result.txt'
errorfile   	=target_dir+'error.txt'

data 	= open(database, 'r')


csvCursor = csv.reader(data)
#沒有result 資料夾的時候
if not os.path.exists(target_dir):
	os.mkdir(target_dir)

result	= open(resultfile,'w')
error 	= open(errorfile,"w")
success_counter=0
error_counter=0

for row in csvCursor:
	old_filename=row[0]
	new_filename=row[1]
	#print(base_filename)
	if(os.path.exists(scan_dir+old_filename)):
		orifile = scan_dir+old_filename
		destfile = target_dir + '/' + new_filename
		shutil.copy(orifile, destfile)
		result.write(old_filename+'已複製\n')
		success_counter+=1
	else:
		error.write(old_filename+'找不到，無法複製\n')
		error_counter+=1
		#將所有檔案關閉

data.close()
result.close()
error.close()

print("已複製%01d筆，未成功複製%01d筆"%(success_counter,error_counter))

