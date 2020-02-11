import socket as sck

s = sck.socket(sck.AF_INET, sck.SOCK_STREAM)
s.connect(("127.0.0.1", 5000))
print("connesso")
stringaDaInviare = "GET http://127.0.0.1:5000/ HTTP/1.1\n\n"
s.sendall(stringaDaInviare.encode())
dataByte = s.recv(4096)
file = open("html.html", 'w')
while dataByte != b'':
    dataByte = s.recv(4096)
    print(dataByte.decode())
    file.write(dataByte.decode())
file.close()
s.close

s = sck.socket(sck.AF_INET, sck.SOCK_STREAM)
s.connect(("127.0.0.1", 5000))
stringaDaInviare = "POST http://127.0.0.1:5000/ HTTP/1.1\r\nContent-Type: application/x-www-form-urlencoded\r\nContent-Length: 25\r\nHost: 127.0.0.1:5000\r\n\r\nusername=boy&password=boy\r\n\r\n"
s.sendall(stringaDaInviare.encode())
dataByte = s.recv(4096)
file = open("html.html", 'w')
while dataByte != b'':
    dataByte = s.recv(4096)
    print(dataByte.decode())
    file.write(dataByte.decode())
file.close()
s.close()

