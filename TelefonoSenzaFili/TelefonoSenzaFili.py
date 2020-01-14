import socket

Host = "0.0.0.0"
HostRicevente = "192.168.10.57"
Porta = 8080

strToSend = ""

sClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Si connette il client precedente

sClient.bind((Host, Porta))
sClient.listen()
conn, addr = sClient.accept()
print("\nSi è connesso: ", addr)

#Mi connetto al server successivo

sServer.connect((HostRicevente, Porta))
print("\nMi sono connesso a: ", HostRicevente)

while True:
    #server
    data = conn.recv(4096)
    strToSend = data.decode()
    print("Messaggio ricevuto dal client precedente: ", strToSend)

    #client
    sServer.sendall(strToSend.encode())
    print("Messaggio inviato al server successivo: ", strToSend)

    if strToSend == "EXIT":
        break

sClient.close()
sServer.close()