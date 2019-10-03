import socket
from threading import Thread

BUFFSIZE = 4096
Server_IP = "127.0.0.1"
Server_PORT = 1234

class ClientThread(Thread):

    def __init__(self, client_ip, client_port):
        Thread.__init__(self)
        self.client_ip = client_ip
        self.client_port = client_port
        print(f"New thread started for {client_ip}, {client_port}")

    def run(self):
        while True:
            data = conn.recv(BUFFSIZE)
            print(f"Server received data: {data.decode()} from {self.client_ip}")
            if(data.decode()) == "exit":
                break
            conn.send("RECEIVED".encode())

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((Server_IP, Server_PORT))
s.listen(5)
ListOfThreads = []
print ("Multithreaded Python server: Waiting for connections from TCP client")

while True:
    (conn, (ip, port)) = s.accept()
    newThread = ClientThread(ip, port)
    newThread.start()
    ListOfThreads.append(newThread)

for t in ListOfThreads:
    t.join()