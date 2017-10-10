#coding:utf-8

import selectors
import socket
import threading,time
import logging

#初始化logging
logger = logging.getLogger("read")
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s %(filename)s %(name)s %(thread)d %(threadName)s [line:%(lineno)d] %(levelname)s %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch);

#初始化httServer
httpServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
httpServer.bind(('127.0.0.1', 8800))
httpServer.listen(5)
httpServer.setblocking(False)



def accept(sock, mask):
    conn,address = sock.accept()
    conn.setblocking(False)
    logger.debug('connect')
    sel.register(conn, selectors.EVENT_READ, read)

def read(conn,mask):
    logger.debug('read')
    data = conn.recv(1024)
    content = ''
    while data:
       content += str(data,'utf-8')
       data = conn.recv(1024)
    if(content.startswith('GET')):
        get(conn,content)
    elif(content.startswith('POST')):
        post(conn,content)
    sel.unregister(conn)

def get(conn,content):
    logger.debug(content)

def post(conn,content):
    logger.debug(content)

#初始化selector并将httpServer注册到selector中
sel = selectors.DefaultSelector()
sel.register(httpServer, selectors.EVENT_READ, accept)

while True:
    events = sel.select()
    for key, mask in events:
        callback = key.data #register时的回调函数
        callback(key.fileobj, mask)

