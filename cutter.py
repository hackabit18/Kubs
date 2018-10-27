import cv2
import json
import os
import cognitive_face as CF
import numpy as np
import sys
import yaml
from PIL import Image, ImageDraw

KEY = os.getenv("KEY")  # Replace with a valid subscription key (keeping the quotes in place).
CF.Key.set(KEY)
# If you need to, you can change your base API url with:
#CF.BaseUrl.set('https://westcentralus.api.cognitive.microsoft.com/face/v1.0/')

BASE_URL = 'https://centralindia.api.cognitive.microsoft.com/face/v1.0/'  # Replace with your regional Base URL
CF.BaseUrl.set(BASE_URL)

f = open("data.json", "r")

video_capture = cv2.VideoCapture("output_wo_rect.avi")
bgr_image = video_capture.read()[1]

data = json.load(f)
os.system("rm faces/*")
# print(data)

f_ = open('temp.json', 'r')
parsed = json.load(f_)

count = 1
for face in data["4"]:
    print count
    rectDict = face["faceRectangle"]
    crop_img = bgr_image[rectDict["top"]:rectDict["top"]+rectDict["height"], rectDict["left"]:rectDict["left"]+rectDict["width"]]
    cv2.imwrite("faces/"+str(count)+".png", crop_img)

    os.system("python track.py face_"+str(count)+" faces/"+str(count)+".png")
    count+=1

print "\n\n-----------\nStarting read:\n\n-----------"
while True:
    ret, bgr_image = video_capture.read()
    if not ret:
        break
    # draw = Image.fromarray(cv2.cvtColor(bgr_image, cv2.COLOR_BGR2RGB))

    # drawhere = ImageDraw.Draw(draw)
    cv2.imwrite("temp.jpg", bgr_image)
    # draw = ImageDraw.Draw(img)
    array = CF.face.detect("temp.jpg")
    flag = False
    for face in array:
        k = CF.face.identify([face['faceId']], "kubss")
        # for face in array:
        #     drawhere.rectangle(getRectangleTuple(face), outline='red')
        try:
            print("k: ", k)
            print("Found: " + parsed[k[0]['candidates'][0]['personId']])
            # tuplehere = getRectangleTuple(face)
            # drawhere.rectangle(tuplehere, outline='green')
            # drawhere.text(tuplehere[0], parsed[k[0]['candidates'][0]['personId']])
        except:
            print("No faces found.")