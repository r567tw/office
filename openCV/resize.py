import cv2
import os

file = input("想要調整大小的圖片：")

img = cv2.imread(file)
size = img.shape
print("原本圖片的大小：")
print(size)
width = int(input("最後輸出的圖片的寬:"))
height = int(input("最後輸出的圖片的高:"))

small = cv2.resize(img, (width, height))

newfile = os.path.splitext(file)
newfileName = newfile[0] + "_resize." + newfile[-1]
cv2.imwrite(newfileName, small)

