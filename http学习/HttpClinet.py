import socket
import threading,time

HOST = '127.0.0.1'
PORT = 8800
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))
time.sleep(2)
msg = bytes('POST index.jsp  HTTP/1.1\r\n fdafda', encoding="utf-8")
client.sendall(msg)
client.close()