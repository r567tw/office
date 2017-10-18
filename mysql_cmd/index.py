import MySQLdb
     
# 連接到 MySQL
db = MySQLdb.connect(host="localhost", user="user", passwd="password", db="database")
db.set_character_set('utf8')
cursor = db.cursor()

with open('name.txt') as fp:
    for line in fp:
        name=line.rstrip()
        # 執行 SQL 語句
        if (name):
            #sql="sql"
            #print(sql)
            cursor.execute(sql)
            result = cursor.fetchone()
            if (result):
                print(result[2]+":"+result[1])
            else:
                print(name+':None')
     
# 輸出結果
#record=cursor.fetchall()
#for record in result:
    #print(record[0])
