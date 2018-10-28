import cv2
import json
import os
import cognitive_face as CF
import numpy as np
import sys
import yaml
from PIL import Image, ImageDraw
import pudb

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
counter = 2

person_wise_emotions = {}
length = int(video_capture.get(cv2.CAP_PROP_FRAME_COUNT))

while True:
    ret, bgr_image = video_capture.read()
    if not ret:
        break

    fout = open("frames_read.txt", "w")
    fout.write(str(counter)+"\n"+str(length)+"\n")
    fout.close()
    print("\n\n")
    print(counter)
    print("")
    counter+=1
    # draw = Image.fromarray(cv2.cvtColor(bgr_image, cv2.COLOR_BGR2RGB))

    # drawhere = ImageDraw.Draw(draw)
    cv2.imwrite("temp.jpg", bgr_image)
    # draw = ImageDraw.Draw(img)
    array = CF.face.detect("temp.jpg", attributes="emotion,age")
    flag = False
    for face in array:
        print face
        k = CF.face.identify([face['faceId']], "kubss")
        # for face in array:
        #     drawhere.rectangle(getRectangleTuple(face), outline='red')
        try:
            print("k: ", k)
            print("Found: " + parsed[k[0]['candidates'][0]['personId']])
            if parsed[k[0]['candidates'][0]['personId']] in person_wise_emotions:
                person_wise_emotions[parsed[k[0]['candidates'][0]['personId']]]["surprised"].append(face["faceAttributes"]["emotion"]["surprise"])
                person_wise_emotions[parsed[k[0]['candidates'][0]['personId']]]["sadness"].append(face["faceAttributes"]["emotion"]["sadness"])
                person_wise_emotions[parsed[k[0]['candidates'][0]['personId']]]["age"].append(face["faceAttributes"]["age"])
            else:
                person_wise_emotions[k[0]['candidates'][0]['personId']] = {}
                person_wise_emotions[k[0]['candidates'][0]['personId']]["surprised"] = []
                person_wise_emotions[k[0]['candidates'][0]['personId']]["sadness"] = []
                person_wise_emotions[k[0]['candidates'][0]['personId']]["age"] = []
            # tuplehere = getRectangleTuple(face)
            # drawhere.rectangle(tuplehere, outline='green')
            # drawhere.text(tuplehere[0], parsed[k[0]['candidates'][0]['personId']])
        except:
            print("No faces found.")

pu.db
final_persons = {}
for person in person_wise_emotions:
    surp = sum(person_wise_emotions[person]["surprised"])
    sad = sum(person_wise_emotions[person]["sadness"])
    final_persons[person] = {}
    if surp > sad:
        emotion_here = "surprised"
    else:
        emotion_here = "sad"
    final_persons[person]["emotion"] = emotion_here
    final_persons[person]["age"] = sum(person_wise_emotions[person]["age"])/len(person_wise_emotions[person]["age"])

f = open("final_persons.json", "w")
json.dumps(final_persons, f)