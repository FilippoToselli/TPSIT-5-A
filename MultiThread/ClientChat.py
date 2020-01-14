import socket
from threading import Thread

NickName = "Toselli"
HOST = "192.168.0.102"
PORT = 2500

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
#AF_INET = IPv4
#SOCK_STREAM = TCP

class ThreadInviare(Thread):
    def __init__(self, s, NickName):
        self.s = s
        Thread.__init__(self)
        print("\nThread Inviare avviato")

    def run(self):
        while True:
            destinatario = input("destinatario:\n>>>")
            stringaDaInviare = input("messaggio:\n>>>")
            s.sendall((destinatario + "§" + NickName + "§" + stringaDaInviare).encode())
            if stringaDaInviare == "exit":
                break
        self.s.close()

class ThreadRicevere(Thread):
    def __init__(self, s):
        self.s = s
        Thread.__init__(self)
        print("\nThread Ricevere avviato")

    def run(self):
        while True:
            data = self.s.recv(4096)
            dataSplit = (data.decode()).split('§')
            print(dataSplit[1] + ": " + dataSplit[2])
            if dataSplit[2] == "exit":
                break
        self.s.close()

newthread = ThreadInviare(s, NickName)
newthread.start()
newthread = ThreadRicevere(s)
newthread.start()