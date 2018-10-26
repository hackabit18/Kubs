import numpy as np
import cv2

cap = cv2.VideoCapture('movie/boring.webm')
addr = "test_images/image.png"

f_no = 1
while(cap.isOpened()):
    ret, frame = cap.read()
    print("saving image to ", addr)
    print("frame no = ", f_no)
    cv2.imshow('display', frame)
    if(f_no%2==0):
    	f_no += 1
    	continue
    cv2.imwrite(addr, frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    f_no += 1

cap.release()
cv2.destroyAllWindows()