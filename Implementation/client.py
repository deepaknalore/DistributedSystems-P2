from gevent import monkey; monkey.patch_all()
import requests
import json
import random

from gevent.pool import Pool

p = Pool(10)

# clemson   utah
CLUSTER = "wisconsin"

CLIENT_ID = "client_1"
SERVER_LIST = ["http://127.0.0.1:5000/", "http://127.0.0.1:5000/"]
payload = {'client_id': CLIENT_ID, 'cluster': CLUSTER}

headers = {
  'Content-Type': 'application/json'
}

def fetch(server):
    response = requests.request("POST", server + "request", headers=headers, data=json.dumps(payload))
    data = response.json()
    print(data)


#initialize
# for server in SERVER_LIST:
#     payload['info'] = random.randrange(1, 1000)
#     fetch(server)

for i in range(100):
    payload['info'] = random.randrange(1, 1000)
    for server in SERVER_LIST:
        p.spawn(fetch,server)
    p.join()

for server in SERVER_LIST:
    requests.request("GET", server + 'filewrite')

