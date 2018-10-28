from flask import Flask, request, Response, jsonify
import os
import requests
import json
from flask_socketio import SocketIO, emit
from flask_cors import CORS
import json


app = Flask(__name__)
CORS(app)
socketio = SocketIO(app)

FLAG = False


def emit_frames(socketio):
	while True:
		f = open("frames_read.txt","r")
		curr = int(f.readline())
		total = int(f.readline())
		try:
			prog = 100.0 * curr/total
		except:
			prog = 0
		if prog>=95.0 or FLAG:	
			break
		print("Emitted")
		print(prog)
		print(curr)
		print(total)
		socketio.emit('statusChange', {"progress" : prog })
		old_prog = prog
		socketio.sleep(0.5)

def analyse(socketio):
	FLAG = False
	f = open("frames_read.txt","w")
	f.write("0\n0\n")
	f.close()
	socketio.start_background_task(emit_frames, socketio)
	os.system("python ../azure_Fac_an.py")
	os.system("python ../eval.py")
	f = open("to_send.json", "r")
	dict_here = f.read()
	dict_here = json.loads(dict_here)
	socketio.emit("statusChange", {"data": dict_here})
	FLAG = True




@app.route('/')
def root():
	return jsonify({"api": "working"})



@app.route('/personData',methods=['GET'])
def upload2():
	# FLAG = False
	# f = open("frames_read.txt","w")
	# f.write("0\n0\n")
	# f.close()
	# socketio.start_background_task(emit_frames, socketio)
	os.system("python ../cutter.py")
	f = open("final_persons.json", "r")
	dict_here = f.read()
	dict_here = json.loads(dict_here)
	# 0socketio.emit("statusChange", {"data_here": dict_here})
	return jsonify(dict_here)
	


@app.route('/upload_video',methods=['POST'])
def upload():
	try:
		
		video = request.files['file']
		with open('video.mp4','wb') as f:
			f.write(video.read())

		video.close()
		# results = analyse(video)
		socketio.start_background_task(analyse,socketio)	
		return (jsonify({"success" : True }), 200, {'Access-Control-Allow-Origin': '*'})
	except Exception as e:
		print(request)
		print(e)
		return (jsonify({"success" : False }), 500, {'Access-Control-Allow-Origin': '*'})


def test_message():
	data = {"z":[[8.83,8.89,8.81,8.87,8.9,8.87],[8.89,8.94,8.85,8.94,8.96,8.92],[8.84,8.9,8.82,8.92,8.93,8.91],[8.79,8.85,8.79,8.9,8.94,8.92],[8.79,8.88,8.81,8.9,8.95,8.92],[8.8,8.82,8.78,8.91,8.94,8.92],[8.75,8.78,8.77,8.91,8.95,8.92],[8.8,8.8,8.77,8.91,8.95,8.94],[8.74,8.81,8.76,8.93,8.98,8.99],[8.89,8.99,8.92,9.1,9.13,9.11],[8.97,8.97,8.91,9.09,9.11,9.11],[9.04,9.08,9.05,9.25,9.28,9.27],[9,9.01,9,9.2,9.23,9.2],[8.99,8.99,8.98,9.18,9.2,9.19],[8.93,8.97,8.97,9.18,9.2,9.18]],"type":"surface"}
	for i in range(101):
		socketio.emit('statusChange', {"progress" : i })
		socketio.sleep(0.1)
	socketio.emit('statusChange', {"data" : data })

@app.route('/socket_end')   ## Heavy function goes here
def ff():
	socketio.start_background_task(test_message)
	return "ok"   


if __name__ == '__main__':
	port = int(os.environ.get("PORT", 5000))  # the app is deployed on heroku
	# app.run(host='0.0.0.0', port=port, debug=True)
	socketio.run(app,debug=True, host='0.0.0.0', port=8081, use_reloader=False)

