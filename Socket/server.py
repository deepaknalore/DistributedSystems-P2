#Taken from: https://www.geeksforgeeks.org/socket-programming-python/
import socket

serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv.bind(('0.0.0.0', 8080))
serv.listen(5)
while True:
    conn, addr = serv.accept()
    from_client = ''
    while True:
        data = conn.recv(4096)
        if not data: break
        from_client += data.decode("utf-8")
        print(from_client)
        conn.send(b"I am SERVER")
    #conn.close()
    print('client disconnected')
