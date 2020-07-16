import pymysql.cursors
from os import listdir,mkdir,getenv
from os.path import isdir,exists
from shutil import copyfile
from dotenv import load_dotenv

load_dotenv()

connection = pymysql.connect(host=getenv('HOST'),
                             user=getenv('USER'),
                             password=getenv('PASSWORD'),
                             db=getenv('DB'),
                             charset=getenv('CHARSET'),
                             cursorclass=pymysql.cursors.DictCursor)

if ( len(listdir("./audio")) ==0):
    print("請於audio資料夾放入檔案")
    exit()

try:
    with connection.cursor() as cursor:
        # Create a new record
        for audio in listdir("./audio"):
            sql = "select id from episodes_table where url = %s"
            cursor.execute(sql,(audio))
            result = cursor.fetchone()
            if (result == None):
                print("找不到此檔案:",audio)
            else:
                if (not isdir("./result/media/in/%s/"%result['id'])):
                    mkdir("./result/media/in/%s"%result['id'])
                copyfile("./audio/%s"%audio, "./result/media/in/%s/%s"%(result['id'],"%s.mp3"%result['id']))
                print("找到此檔案:%s, 並整理到相對應的資料夾."%audio)

finally:
    connection.close()