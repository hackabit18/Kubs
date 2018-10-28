import json
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import pyplot as plt
import numpy as np
import pudb

with open('data.json', 'r') as fp:
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
	rt = 0
	count = 0.0
	for face in data[str(fr)]:
		hp += face["faceAttributes"]["emotion"]["happiness"]
		sd += face["faceAttributes"]["emotion"]["sadness"]
		sr += face["faceAttributes"]["emotion"]["surprise"]
		rt += 1 - (face["faceAttributes"]["emotion"]["happiness"] + face["faceAttributes"]["emotion"]["sadness"] + face["faceAttributes"]["emotion"]["surprise"])
		count += 1
	happiness.append(hp/count)
	sadness.append(sd/count)
	surprise.append(sr/count)

# plt.plot(f_no, happiness, color ='green', linewidth = 2)
# plt.plot(f_no, sadness, color = 'red', linewidth = 2)
# plt.plot(f_no, surprise, color = 'blue', linewidth = 2)

# plt.show()
# pu.db
to_send = {}
to_send["happy_per"] = 100.0 * sum(happiness) / len(happiness)
to_send["surprise_per"] = 100.0 * sum(surprise) / len(surprise)
to_send["sad_per"] = 100.0 * sum(sadness) / len(sadness)
to_send["happiness"] = happiness
to_send["surprise"] = surprise
to_send["sadness"] = sadness
to_send["time"] = f_no

f = open("to_send.json", "w")
json.dump(to_send, f)