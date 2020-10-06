import pymysql
import os
from dotenv import load_dotenv

# 資料庫連線設定
load_dotenv()
db = pymysql.connect(
    host=os.getenv("DBHOST"),
    user=os.getenv("DBUSER"),
    passwd=os.getenv("PASSWORD"),
    port=int(os.getenv("PORT")),
    db=os.getenv("DB"),
    charset=os.getenv("CHARSET"),
)

# 建立操作游標(將result 改為 字典)
cursor = db.cursor(pymysql.cursors.DictCursor)

# 根據資料庫語法
with open("scripts.txt") as scripts:
    for script in scripts:
        script = script.rstrip()
        # 執行 SQL 語句
        cursor.execute(script)
        # 選取第一筆結果
        result = cursor.fetchone()
        # 選取多筆筆結果
        # result = cursor.fetchall()
        # print(len(result))
        print(result)
# 關閉連線
db.close()

