from flask import Flask, request, Response, jsonify
import os
import requests
import json
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)


@app.route('/')
def root():
	return jsonify({"api": "working"})


@app.route('/upload_video',methods=['POST','OPTIONS'])
def upload():
	try:
		
		video = request.files['file']
		with open('video.mp4','wb') as f:
			f.write(video.read())

		# results = analyse(video)
		video.close()
		return ("ok", 200, {'Access-Control-Allow-Origin': '*'})
	except Exception as e:
		print(request)
		print(e)
		return "not ok"


def test_message():
	for i in range(10):
		socketio.emit('myevent', 'somedata')
		socketio.sleep(2)

@app.route('/socket_end')   ## Heavy function goes here
def ff():
	socketio.start_background_task(test_message)
	return "ok"   


if __name__ == '__main__':
	port = int(os.environ.get("PORT", 5000))  # the app is deployed on heroku
	# app.run(host='0.0.0.0', port=port, debug=True)
	socketio.run(app,debug=True, host='localhost', port=8081, use_reloader=False)
