import cv2
import json
import os

f = open("data.json", "r")

video_capture = cv2.VideoCapture("output_wo_rect.avi")
bgr_image = video_capture.read()[1]

data = json.load(f)
os.system("rm faces/*")
# print(data)
count = 1
for face in data["4"]:
	print count
	rectDict = face["faceRectangle"]
	crop_img = bgr_image[rectDict["top"]:rectDict["top"]+rectDict["height"], rectDict["left"]:rectDict["left"]+rectDict["width"]]
	cv2.imwrite("faces/"+str(count)+".png", crop_img)

	os.system("python track.py face_"+str(count)+" faces/"+str(count)+".png")
	count+=1