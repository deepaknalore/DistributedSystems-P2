#Taken from: https://www.geeksforgeeks.org/socket-programming-multi-threading-python/
# Import socket module 
import time
import socket 
import argparse
from datetime import datetime

ipList = ["c220g1-030811.wisc.cloudlab.us", "ms0619.utah.cloudlab.us", "clnode216.clemson.cloudlab.us"]


def Main(args): 
	# local host IP '127.0.0.1' 
	host = '127.0.0.1'

	# Define the port on which you want to connect 
	port = 12345

	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 

	# connect to server on local computer 
	s.connect((args.server_host,port)) 

	start_time = time.time()
	number_of_minutes = 10

	while time.time() < (start_time + (60 * number_of_minutes)):
		# message you send to server
		#message = "I am the client speaking "

		# message sent to server 
		#client_id = input("Enter the client id for testing purpose\n")
		#message = message + str(client_id)
		message = "Hi"
		time_to_log = datetime.utcnow()
		time_before_send = time.time()
		s.send(message.encode('ascii')) 

		# messaga received from server 
		data = s.recv(1024)
		print(data)
		time_after_receive = float(data.decode('ascii').split(':')[1].strip(' '))
		latency = ((time_after_receive - time_before_send)*1000) / 2.0

		with open(str(args.server_host) + ".csv", "a") as fd:
			fd.write(str(time_to_log) + "," + str(latency) + "\n")

	s.close() 

if __name__ == '__main__': 
	parser = argparse.ArgumentParser(description='To get the server host')
	parser.add_argument('--server_host', type=str, default='127.0.0.1')
	args = parser.parse_args()
	print(args.server_host)
	Main(args) 
