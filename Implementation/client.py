import requests
import csv
import json
import time

CLIENT_ID = "client_1"
SERVER_LIST = ["http://127.0.0.1:5000/"]
payload = {'client_id': CLIENT_ID, 'info': ''}

headers = {
  'Content-Type': 'application/json'
}

payload['info'] = 'hello'
for server in SERVER_LIST:
    response = requests.request("POST", server + "request", headers=headers, data=json.dumps(payload))
    data = response.json()
    print(data)

