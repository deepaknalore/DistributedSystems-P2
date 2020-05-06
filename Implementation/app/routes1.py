from app import app
from datetime import datetime
from flask import request, render_template, jsonify, make_response, abort
from collections import defaultdict
from _thread import *
import time

import logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

my_server_id = "wisconsin"
my_cluster = "wisconsin"
servers = ['wisconsin', 'clemson', 'utah']
log = []

latency_dict = defaultdict(dict)
# latency_dict['wisconsin']['wisconsin'] = 0.08
# latency_dict['wisconsin']['clemson'] = 12.5
# latency_dict['wisconsin']['utah'] = 17.5
# latency_dict['clemson']['clemson'] = 0.02
# latency_dict['clemson']['wisconsin'] = 13.0
# latency_dict['clemson']['utah'] = 25.0
# latency_dict['utah']['utah'] = 0.3
# latency_dict['utah']['wisconsin'] = 18.0
# latency_dict['utah']['clemson'] = 25.0

latency_dict['wisconsin']['wisconsin'] = 82
latency_dict['wisconsin']['clemson'] = 12512
latency_dict['wisconsin']['utah'] = 17534
latency_dict['clemson']['clemson'] = 22
latency_dict['clemson']['wisconsin'] = 13056
latency_dict['clemson']['utah'] = 25124
latency_dict['utah']['utah'] = 326
latency_dict['utah']['wisconsin'] = 18822
latency_dict['utah']['clemson'] = 25024


def handleRequest(client_id, client_cluster, info):
    my_latency = latency_dict[client_cluster][my_cluster]
    all_latencies = []
    for server in servers:
        all_latencies.append(latency_dict[client_cluster][server])
    max_latency = max(all_latencies)
    if client_cluster == "clemson":
        max_latency = 100000.0
    append_message = str(client_cluster) + ":" + str(client_id) + ":" + str(info)
    
    add_time = time.time() + (max_latency - my_latency + 2000)*(10**(-6))
    while time.time() < add_time:
        continue
    log.append(append_message)
    return

@app.route('/filewrite', methods = ['GET'])
def fileWriter():
    global log
    with open(my_server_id + "." + "log", 'w') as f:
        for entry in log:
            f.write(entry + "\n")
    log = []
    return jsonify({"Request": True}), 200


@app.route('/request', methods = ['POST'])
def endpoint():
    if not request.json or not 'client_id' in request.json or not 'info' in request.json:
        abort(400)
    try:
        client_id = request.json['client_id']
        client_cluster = request.json['cluster']
        info = request.json['info']
        my_latency = latency_dict[client_cluster][my_cluster]
        max_latency = my_latency
        for server in servers:
            max_latency = max(max_latency, latency_dict[client_cluster][server])
        append_message = str(client_cluster) + ":" + str(client_id) + ":" + str(info)
        time.sleep((max_latency - my_latency + 4000)*(10**(-6)))
        log.append(append_message)
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







