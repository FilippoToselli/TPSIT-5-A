import socket

HOST = "0.0.0.0"
PORT = 65432
strToSend = ""

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#AF_INET = IPv4
#SOCK_STREAM = TCP

s.bind((HOST, PORT))
s.listen()
conn, addr = s.accept()
print("\nSi è connesso: ", addr)

while True:
    data = conn.recv(4096)

    print("Messaggio ricevuto dal client: ", data.decode())

    if data.decode() == "0":
        break

    strToSend = input("\n> Stringa da inviare ('0' per uscire): ")

    conn.sendall(strToSend.encode())

    if strToSend == "0":
        break

s.close()
print("Connessione chiusa")