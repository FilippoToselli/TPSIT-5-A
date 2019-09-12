import socket

HOST = "192.168.10.73"
PORT = 65432
strToSend = ""

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#AF_INET = IPv4
#SOCK_STREAM = TCP

s.connect((HOST, PORT))

while True:
    strToSend = input("\n> Stringa da inviare ('0' per uscire): ")

    s.sendall(strToSend.encode())

    if strToSend == "0":
       break

    data = s.recv(4096)
    
    print("\nMessagio ricevuto dal server: ", data.decode())

    if data.decode() == "0":
       break

s.close()
print("Connessione chiusa")