from flask import Flask, request, Response, jsonify
import os
import requests
import json

app = Flask(__name__)

@app.route('/')
def root():
	return jsonify({"api": "working"})

if __name__ == '__main__':
	port = int(os.environ.get("PORT", 5000))  # the app is deployed on heroku
	app.run(host='0.0.0.0', port=port, debug=True)
