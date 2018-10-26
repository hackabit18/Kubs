from flask import Flask, request, Response, jsonify
import os
import requests
import json

app = Flask(__name__)

@app.route('/')
def root():
	return jsonify({"api": "working"})


# <form class="form-group" action="/upload" method = "POST" enctype = "multipart/form-data" >
#              <input class="form-control" type = "file" name = "file" />  <br>
#              <input class="btn btn-primary" type = "submit"/>  <br>
#           </form>       


@app.route('/upload_video',methods=['POST'])
def upload():
	try:
		video = request.files['file']
		## video si in binary form which can be directly used by opencv to extract frames
		with open('video.mp4','wb') as f:
			f.write(video.read())

		# results = analyse(video)
		video.close()
		return "ok"
	except Exception as e:
		print(e)
		return "not ok"



if __name__ == '__main__':
	port = int(os.environ.get("PORT", 5000))  # the app is deployed on heroku
	app.run(host='0.0.0.0', port=port, debug=True)
