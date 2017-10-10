#coding:utf-8

from selectors import DefaultSelector, EVENT_WRITE
import re

#创建选择器
selector = DefaultSelector()
#创建sockte
sock = socket.socket()
#设置socket为非阻塞
sock.setblocking(False)
try:
    sock.connect(('xkcd.com', 80))
except BlockingIOError:
    pass

def connected():
    selector.unregister(sock.fileno())
    print('connected!')

selector.register(sock.fileno(), EVENT_WRITE, connected)


def loop():
    while True:
        events = selector.select()
        for event_key, event_mask in events:
            callback = event_key.data
            callback()