import cv2
import os

file = input("想要灰階的圖片：")
img = cv2.imread(file, cv2.IMREAD_GRAYSCALE)
newfile = os.path.splitext(file)
newfileName = newfile[0] + "_gray." + newfile[-1]
cv2.imwrite(newfileName, img)

