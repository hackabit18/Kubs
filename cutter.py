import cv2
import json

f = open("data.json", "r")

video_capture = cv2.VideoCapture("output.avi")
bgr_image = video_capture.read()[1]

data = json.load(f)

# print(data)
count = 1
for face in data["4"]:
	print count
	rectDict = face["faceRectangle"]
	crop_img = bgr_image[rectDict["top"]+2:rectDict["top"]+rectDict["height"]-2, rectDict["left"]+2:rectDict["left"]+rectDict["width"]-2]
	cv2.imwrite("faces/"+str(count)+".png", crop_img)
	count+=1
