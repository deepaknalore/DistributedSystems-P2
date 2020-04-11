from app import app
from datetime import datetime
from flask import request, render_template, jsonify, make_response, abort
from collections import defaultdict
from _thread import *
import threading 
import argparse
import time 
import json


my_server_id = "wisconsin"
my_cluster = "wisconsin"
servers = ['wisconsin', 'clemson', 'utah']
log = []

# @app.route('/')
# @app.route('/index')
# def index():
#     return "Hello, World!"
latency_dict = defaultdict(dict)
latency_dict['wisconsin']['wisconsin'] = 0.08
latency_dict['wisconsin']['clemson'] = 12.5
latency_dict['wisconsin']['utah'] = 17.5
latency_dict['clemson']['clemson'] = 0.02
latency_dict['clemson']['wisconsin'] = 13
latency_dict['clemson']['utah'] = 25
latency_dict['utah']['utah'] = 0.3
latency_dict['utah']['wisconsin'] = 18
latency_dict['utah']['clemson'] = 25


def handleRequest(client_id, client_cluster, info):
    # print("In handleRequest")
    # print(client_id)
    # print(client_cluster)
    # print(my_cluster)
    my_latency = latency_dict[client_cluster][my_cluster]
    all_latencies = []
    for server in servers:
        all_latencies.append(latency_dict[client_cluster][server])
    max_latency = max(all_latencies)
    append_message = str(client_cluster) + ":" + str(client_id) + ":" + str(info)
    if max_latency == my_latency:
        log.append(append_message)
    else:
        add_time = time.time() + (max_latency - my_latency)*(10**(-3))
        while time.time() < add_time:
            continue
        log.append(append_message)
    return

@app.route('/filewrite', methods = ['GET'])
def fileWriter():
    with open(my_server_id + "." + "log", 'a') as f:
        for entry in log:
            f.write(entry)


@app.route('/request', methods = ['POST'])
def endpoint():
    if not request.json or not 'client_id' in request.json or not 'info' in request.json:
        abort(400)
    try:
        client_id = request.json['client_id']
        client_cluster = request.json['cluster']
        info = request.json['info']
        start_new_thread(handleRequest, (client_id, client_cluster, info,)) 
        return jsonify({"Request": True}), 200
    except Exception as e:
        print(e)
    return jsonify({"Request": False}), 500


# @app.route('/initialize', methods = ['GET'])
# def initialize():
#     print("In main")
#     parser = argparse.ArgumentParser(description='To get the server host')
#     parser.add_argument('--server_id', type=str, default='wisconsin', description='Please enter the server cluster')
#     args = parser.parse_args()
#     my_server_id = str(args.server_id)
#     my_server_cluster = str(args.server_id)
#     start_new_thread(fileWriter, f())







