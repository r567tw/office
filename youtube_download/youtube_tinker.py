import tkinter as tk
from pytube import YouTube
 
def clickUrl():
    global listvideo, listradio
    labelMsg.config(text="")
    if(url.get()==""):
        labelMsg.config(text="請輸入網址")
    else:
        try:
            yt.url=url.get()
            rbvalue=1
            for v1 in yt.get_videos():
                listvideo.append(v1)
            for v2 in listvideo:
                rbtem = tk.Radiobutton(frame3,text=v2,variable=video,value=rbvalue,command=rbVideo)
                if (rbvalue==1):
                    rbtem.select()
                listradio.append(rbtem)
                rbtem.grid(row=rbvalue-1,column=0,sticky="w")
                rbvalue+=1
            btnDown.config(state="normal")
        except:
            labelMsg.config(text="找不到該youtube 影片")
            


def clickDown():
    global getvideo,strftype,listradio
    getvideo.download('.')
    for r in listradio:
        r.destroy()
    listradio.clear()
    listvideo.clear()
    url.set("")
    labelMsg.config(text="下載完成")

def rbVideo():
    global getvideo,strftype
    labelMsg.config(text="")
    strvideo = str(listvideo[video.get()-1])
    start1=strvideo.find("(.")
    end1 = strvideo.find(")")
    strftype= strvideo[start1+2:end1]
    end2=strvideo.rfind(" - ")
    strresolution=strvideo[end1+4 : end2]
    getvideo=yt.get(strftype,strresolution)

getvideo=""
strftpe=""
listvideo=[]
listradio =[]
yt=YouTube()
win = tk.Tk()
win.geometry("450x320")
win.title('下載Youtube影片')
video = tk.IntVar()
url = tk.StringVar()
frame1= tk.Frame(win,width=450)
frame1.pack()
label1=tk.Label(frame1,text="Youtube 網址:")
entryUrl = tk.Entry(frame1,textvariable=url)
entryUrl.config(width=40)
btnUrl=tk.Button(frame1,text="確定",command=clickUrl)
label1.grid(row=0,column=0,sticky="e")
entryUrl.grid(row=0,column=1)
btnUrl.grid(row=0,column=2)


frame2=tk.Frame(win)
frame2.pack()
btnDown = tk.Button(frame2,text="下載影片",command=clickDown)
btnDown.pack(pady=6)
btnDown.config(state="disabled")

labelMsg = tk.Label(win, text="", fg="red")
labelMsg.pack()

frame3 =tk.Frame(win)
frame3.pack()

win.mainloop()

