import json
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import pyplot as plt
import numpy as np

with open('data_boring.json', 'r') as fp:
    data = json.load(fp)

f_no = []
happiness = []
sadness = []
surprise = []

for fr in data:
	f_no.append(int(fr))

f_no = sorted(f_no)

for fr in sorted(f_no):
	print(fr)
	# f_no.append(fr)
	hp = 0
	sd = 0
	sr = 0
	count = 0.0
	for face in data[str(fr)]:
		hp += face["faceAttributes"]["emotion"]["happiness"]
		sd += face["faceAttributes"]["emotion"]["sadness"]
		sr += face["faceAttributes"]["emotion"]["surprise"]
		count += 1
	happiness.append(hp/count)
	sadness.append(sd/count)
	surprise.append(sr/count)

plt.plot(f_no, happiness, color ='green', linewidth = 2)
plt.plot(f_no, sadness, color = 'red', linewidth = 2)
plt.plot(f_no, surprise, color = 'blue', linewidth = 2)

plt.show()