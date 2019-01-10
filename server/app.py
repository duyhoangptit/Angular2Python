#server/app.py

import json
import logging

from flask import Flask
from flask import Blueprint, Response, jsonify, make_response, request

app = Flask(__name__, static_folder="../front/dist/front",static_url_path="")

@app.route("/")
def helloworld():
	return "Hello World!"

@app.route("/home")
def home():
	return make_response(open('../front/dist/front/index.html').read())

if __name__=='__main__':
	app.run(debug=True, port=8000, host='localhost')