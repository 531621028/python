import socket
tin=socket.socket()
tin.connect(('127.0.0.1',8800))
while True:
    inp=input('>>>>')
    tin.send(inp.encode('utf8'))
    data=tin.recv(1024)
    print(data.decode('utf8'))