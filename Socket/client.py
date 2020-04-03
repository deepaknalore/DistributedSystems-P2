#Taken from: https://www.geeksforgeeks.org/socket-programming-python/
import socket
import time
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('0.0.0.0', 8080))
count = 1
while True:
	count += 1
	if count == 5:
		client.close()
	client.send(b"I am CLIENT")
	time.sleep(5)
	from_server = client.recv(4096).decode("utf-8")
	#client.close()
	print(from_server)