import pyautogui
import time

keyname = input('想要哪個按鍵被連續點擊：')
clicktime = int(input('需要連續幾次: '))

print('你所設定的連續點擊 %s 鍵 %s 次將在30秒後被執行'%(keyname,clicktime))
time.sleep(30)
pyautogui.PAUSE = 1
for i in range(clicktime):
    pyautogui.keyDown(keyname)
