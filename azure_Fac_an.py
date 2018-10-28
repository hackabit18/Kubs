########### Python 3.2 #############
import requests
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from io import BytesIO
from PIL import Image
import cv2
import os
from copy import copy
# import util

headers = {
    # Request headers
    'Ocp-Apim-Subscription-Key': os.getenv("KEY"),
    'Content-Type': 'application/octet-stream'
}

params = {
    # Request parameters
    'returnFaceId': 'true',
    'returnFaceLandmarks': 'false',
    'returnFaceAttributes': 'age,emotion',
}

url = "https://centralindia.api.cognitive.microsoft.com/face/v1.0/detect";

cap = cv2.VideoCapture('video.mp4')
# addr = "test_images/image.png"

fwidth = 1280
fheight = 544
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output_now.avi',fourcc, 5.0, (fwidth,fheight))
out_wo_rect = cv2.VideoWriter('output_now_wo_rect.avi',fourcc, 5.0, (fwidth,fheight))

f_no = 1
ratio = 4

save_dict = {}
import json
with open('data.json', 'w') as fp:
    json.dump(save_dict, fp)

length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

while(cap.isOpened()):
    ret, frame = cap.read()
    frame_cp = copy(frame)
    # print(frame.shape)
    print("frame = ", f_no)
    f = open("frames_read.txt", "w")
    f.write(str(f_no)+"\n")
    f.write(str(length)+"\n")
    f.close()
    f_no += 1
    if(f_no%ratio!=0):
        continue
    cv2.imwrite("test_images/test.png", frame)
    f = open('test_images/test.png','rb')
    image_data = f.read()
    res = requests.post(url, headers=headers, params=params, data=image_data)
    analysis = res.json()

    try:
        for face in analysis:
            fr = face["faceRectangle"]
            em = face["faceAttributes"]["emotion"]
            origin = (fr["left"], fr["top"])
            dest = (fr["left"]+fr["width"], fr["top"]+fr["height"])
            cv2.rectangle(frame, origin, dest, color = (0,255,0))

        # cv2.imshow('display', frame)
        if ret==True:
            # frame = cv2.flip(frame,0)
            for i in range(ratio):
                out.write(frame)
                out_wo_rect.write(frame_cp)
                save_dict[f_no+i] = analysis
            cv2.waitKey(1)
        else:
            break
    except:
        break

cap.release()
out.release()
cv2.destroyAllWindows()

import json
with open('data.json', 'w') as fp:
    json.dump(save_dict, fp)


