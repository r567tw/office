# office

![test](https://github.com/r567tw/office/workflows/test/badge.svg?branch=master)

> 開發簡單的辦公室辦公相關或一些雜七雜八的自動化任務工具

## Before use these tools:

```
{For mac}
virtualenv .env_office

source .env_office/bin/activate
//啟動office python的虛擬環境，確保自己可以使用的packages...

pip freeze > .env_office/requirements.txt
//將目前的module 輸出到 .env_office/requirements.txt 這個檔案當中。

pip install -r .env_office/requirements.txt
//安裝一下需要使用的套件

deactivate
// 離開虛擬環境
```

## Indexs

1. goolge_map

   > 藉由 CSV(第一欄 代號，第二欄地址或者名稱) 抓出 GOOGLE MAP 的截圖

2. id_card_number

   > 台灣身分證字號的驗證與檢查還有產生

3. web_auto

   > 網頁表單的自動化撰寫

4. youtube_download

   > youtube 影片下載
   >
   > - tinker 簡易版
   > - 讀取 json 多個版

5. file_manager 檔案管理類

   > - 找出重複的圖片 刪除複製輸出
   > - 找出符合副檔名的檔案，全部複製出來
   > - 找出符合自己設定的檔名清單，全部找出來並告訴你哪裡沒有找出來的
   > - 藉著同目錄的 csv 檔規則，批次修改檔名

6. search_key_word

   > 從多個文字檔裡找出關鍵字

7. mysql_cmd

   > 連接 mysql 輸出資料

8. json

   > formater : 想要觀看
   > editor : 做 json 的編輯
   > 以撰寫非常 simple 的模樣～

9. action_auto

   > 利用 pyautogui 自動化我們操作電腦的動作
   > <br/>autoclick：　連點器
   > <br/>autoinputNumber: 幫我輸入從開始到結束後的數字並且每次輸入完按下我指定的按鍵
   > <br/>autoinputType: 幫我輸入每次一樣的內容並且每次輸入完按下我指定的按鍵

10. pattern_matching

    > 幫助兩個檔案協尋符合正規表達式的規格 pattern。從而求出其中差集、交集、並集...等

11. auto_modify

```
自動幫我可以自動化一連串的動作，並依照我要的template 產生我想要的程式碼。
```

12. line_stock

```
根據python 技術者這本書，寫一個line bot 可以盯盤股票的程式。
```

13. threading

```
練習多執行緒議題，還不是搞得很清楚～
```

14. httpd_related

```
工作用常常會修改httpd 相關設定與apache 重開等工作，使用python 寫script 自動化！
```

15. bitcoins

```
玩玩關於比特幣歷史價格趨勢、MA線、學習pandas以及matplotlib 畫圖。
```

16. openCV

```
玩一玩openCV 圖片處理，順便弄個灰階、調整大小的處理程式，順便玩玩圖像辨識。___capture.py 並未完成，似乎儲存之後出現一些狀況
```

# Other

目前 pytube 9.5.1 有些問題
可以參考以下[連結](https://www.flag.com.tw/bk/t/ft700)
如果使用.env_office 可至

```
.env_office/lib/python3.6/site-packages/pytube/__main__.py
.env_office/lib/python3.6/site-packages/pytube/streams.py
```
