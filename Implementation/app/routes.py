from app import app
from datetime import datetime
from flask import request, render_template, jsonify, make_response, abort
import json

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

def myconverter(o):
    if isinstance(o, datetime):
        return o.__str__()

@app.route('/request', methods = ['POST'])
def endpoint():
    if not request.json or not 'client_id' in request.json or not 'info' in request.json:
        abort(400)
    try:
        client_id = request.json['client_id']
        info = request.json['info']
        return jsonify({"Request": True}), 200
    except Exception as e:
        print(e)
    return jsonify({"Request": False}), 500