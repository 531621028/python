#coding:utf-8

import selectors
import socket
import logging


logging.basicConfig(level=logging.DEBUG,format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
logging.debug('This is debug message')

sel = selectors.DefaultSelector()

def accept(sock, mask):
    conn, addr = sock.accept()  # Should be ready
    logging.debug('accepted'+str(conn)+'from'+str(addr))
    conn.setblocking(False)
    sel.register(conn, selectors.EVENT_READ, read)

def read(conn, mask):
    data = conn.recv(1000)  # Should be ready
    if data:
        logging.debug('echoing'+repr(data)+'to'+str(conn))
        conn.send(data)  # Hope it won't block
    else:
        logging.debug('closing'+str(conn))
        sel.unregister(conn)
        conn.close()

sock = socket.socket()
sock.bind(('127.0.0.1', 8800))
sock.listen(100)
sock.setblocking(False)
sel.register(sock, selectors.EVENT_READ, accept)

while True:
    events = sel.select()
    for key, mask in events:
        print(str(key))
        callback = key.data #register时的回调函数
        #logging.debug('回调函数名称',callback.__name__)
        callback(key.fileobj, mask)
