import json
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import pyplot as plt
import numpy as np

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
	count = 0.0
	for face in data[str(fr)]:
		hp += face["faceAttributes"]["emotion"]["happiness"]
		sd += face["faceAttributes"]["emotion"]["sadness"]
		sr += face["faceAttributes"]["emotion"]["surprise"]
		count += 1
	happiness.append(hp/count)
	sadness.append(sd/count)
	surprise.append(sr/count)

# plt.plot(f_no, happiness, color ='green', linewidth = 2)
# plt.plot(f_no, sadness, color = 'red', linewidth = 2)
# plt.plot(f_no, surprise, color = 'blue', linewidth = 2)
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')

# x_grid = np.linspace(0, max(surprise), 100*len(surprise))
# y_grid = np.linspace(0, max(sadness), 100*len(sadness))
# B1, B2 = np.meshgrid(x_grid, y_grid, indexing='xy')
# Z = np.zeros((len(surprise), len(f_no)))

from scipy import interpolate

xx, yy = np.meshgrid(surprise, sadness)

# print "here1"
# f = interpolate.interp2d(surprise, sadness, f_no, kind='quintic')
# print "here2"

# xnew = np.arange(min(min(surprise), min(sadness)), max(max(surprise), max(sadness)), 0.01)
# ynew = np.arange(min(min(surprise), min(sadness)), max(max(surprise), max(sadness)), 0.01)

# znew = f(xnew, ynew)

# Z = spline(B1,B2)
# fig = plt.figure(figsize=(10,6))
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(surprise,sadness,f_no, c='r')

ax.set_xlabel('Surprise')
ax.set_ylabel('Sadness')
ax.set_zlabel('Time')
ax.set_xlim3d(0, 0.6)
ax.set_ylim3d(0,0.05)
ax.set_zlim3d(0,150)
plt.show()