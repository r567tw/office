from time import sleep
import json
import os
import tkinter as tk
from pytube import YouTube


def clickUrl():
    with open("youtube.json", "r") as reader:
        jf = json.loads(reader.read())
        data = jf["urls"]
        for url in data:
            print(url)
            try:
                video = YouTube(url).streams.first().download("./youtube")
                labelMsg.config(text="下載完成")
            except:
                labelMsg.config(text="出現了一些錯誤")


dname = "youtube"
if not os.path.exists(dname):
    os.mkdir(dname)
win = tk.Tk()
win.geometry("450x320")
win.title("下載許多Youtube影片")
url = tk.StringVar()
frame1 = tk.Frame(win, width=450)
frame1.pack()
btnUrl = tk.Button(frame1, text="確定下載", command=clickUrl)
btnUrl.grid(row=0, column=2)
labelMsg = tk.Label(win, text="", fg="red")
labelMsg.pack()
labelDescription = tk.Label(win, text="讀取檔案裡的youtube.json，批次下載youtube 影片", fg="red")
labelDescription.pack()

win.mainloop()
