import pyautogui
import time

times = int(input('輸入多少次: '))
content = input('希望輸入什麼內容')
keyName = input('請問每次內容輸入完需要按下哪個按鍵: ')

print('你所設定的動作將在5秒後被執行')
time.sleep(5)
pyautogui.PAUSE = 1
for i in range(1, times+1):
    pyautogui.typewrite(content, interval=0.25)
    pyautogui.keyDown(keyName)
