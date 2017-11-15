import csv
import os
import sys
import shutil

class filefilter(object):

	database	=''
	scan_dir	=''
	target_dir	=''

	result		=''
	error   	=''

	def __init__(self, CSVdata,ScanedDir,TargetDir):
		self.database 	= CSVdata
		base_dir		= os.path.dirname(CSVdata)
		#print('data_base_dir:'+base_dir);
		if base_dir == '':
			base_dir=os.getcwd()
		self.result		= base_dir+'/'+'result.txt'
		self.error 		= base_dir+'/'+'error.txt'
		if ScanedDir.endswith('/'):
			self.scan_dir 	= ScanedDir
		else:
			self.scan_dir	= ScanedDir+'/'

		if TargetDir.endswith('/'):
			self.target_dir	= TargetDir
		else:
			self.target_dir = TargetDir+'/'

	def process(self):
		scan_dir	= self.scan_dir
		target_dir	= self.target_dir

		data 	= open(self.database, 'r')
		result 	= open(self.result,'w')
		error 	= open(self.error,'w')
		success_counter=0;
		error_counter=0;

		csvCursor = csv.reader(data)
		#沒有result 資料夾的時候
		if not os.path.exists(target_dir):
		    os.mkdir(target_dir)
		for row in csvCursor:
		    base_filename=row[0]
		    #print(base_filename)
		    if(os.path.exists(scan_dir+base_filename)):
		        orifile = scan_dir+base_filename
		        destfile = target_dir + '/' + base_filename
		        shutil.copy(orifile, destfile)
		        result.write(base_filename+'已複製\n')
		        success_counter+=1
		    else:
		        error.write(base_filename+'找不到，無法複製\n')
		        error_counter+=1
		#將所有檔案關閉
		data.close();
		result.close();
		error.close();

		return "已複製%01d筆，未成功複製%01d筆"%(success_counter,error_counter);


#filter = filefilter('data/files.csv','photo/','result/')
#print(filter.process())
