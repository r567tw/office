import tkinter as tk;
#調用自己的函數
import filefilter;

def btnGetResult():
	global databaseEntry,scandirEntry,targetdirEntry,msg;
	data = databaseEntry.get()
	scandir = scandirEntry.get()
	targetdir = targetdirEntry.get()

	a_filter = filefilter.filefilter(data,scandir,targetdir)
	result = a_filter.process()
	print(result)
	msg.delete('1.0', tk.END)
	result+='\n結果在result.txt；錯誤在error.txt';
	msg.insert(tk.INSERT,result)



window=tk.Tk();
window.geometry("1000x600")
window.title("過濾檔案")

frame1= tk.Frame(window,width=1000)
frame1.pack()

label=tk.Label(frame1, text="過濾檔案")   #建立標籤物件
label.pack()#顯示元件

labeldatabase=tk.Label(frame1, text="資料清單(需用csv 檔)")   #建立標籤物件
labeldatabase.pack()#顯示元件
databaseEntry = tk.Entry(frame1,text='data/files.csv')
databaseEntry.pack()

labelscan=tk.Label(frame1, text="要掃描的資料夾")   #建立標籤物件
labelscan.pack()#顯示元件
scandirEntry = tk.Entry(frame1,text='photo/')
scandirEntry.pack()

labeltarget=tk.Label(frame1, text="要輸出的資料夾")   #建立標籤物件
labeltarget.pack()#顯示元件
targetdirEntry = tk.Entry(frame1,text='output/')
targetdirEntry.pack()

button=tk.Button(frame1, text="過濾",command=btnGetResult)
button.pack()     #顯示元件

msg = tk.Text(frame1)
msg.pack()

window.mainloop();




