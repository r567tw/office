import cv2

capture = cv2.VideoCapture(0)
img_pre = None  # 前影像, 預設是空的
i = 0
while capture.isOpened():
    success, img = capture.read()
    if success:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 灰階處理
        img_now = cv2.GaussianBlur(gray, (13, 13), 5)  # 高斯模糊
        if img_pre is not None:  # ←如果前影像不是空的, 就和前影像比對
            diff = cv2.absdiff(img_now, img_pre)  # 此影格與前影格的差異值
            ret, thresh = cv2.threshold(diff, 25, 255, cv2.THRESH_BINARY)  # 門檻值
            contours, _ = cv2.findContours(
                thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE  # 找到輪廓
            )
            if contours:  # 如果有偵測到輪廓
                i = i + 1
                cv2.drawContours(img, contours, -1, (255, 255, 255), 2)
                print("偵測到移動" + str(i) + "次")

            # else:
            #     # print("靜止畫面")

        cv2.imshow("frame", img)
        img_pre = img_now.copy()
    k = cv2.waitKey(50)
    if k == ord("q"):
        cv2.destroyAllWindows()
        capture.release()
        break

