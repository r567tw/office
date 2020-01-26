# -*- coding: utf-8 -*
import pyautogui
import time

start = int(input("數字從多少開始數: "))
end = int(input("數字到多少結束: "))
keyName = input("請問每次數字輸入完需要按下哪個按鍵: ")

print("你所設定的動作將在5秒後被執行")
time.sleep(5)
pyautogui.PAUSE = 1
for i in range(start, end + 1):
    content = str(i)
    pyautogui.typewrite(content, interval=0.25)
    pyautogui.keyDown(keyName)

