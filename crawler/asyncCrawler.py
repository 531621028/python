#coding:utf-8

import re
import socket
import selectors
import traceback

urls_todo = set(['/'])
seen_urls = set(['/'])

class Future:
    def __init__(self):
        self.result = None
        self._callbacks = []

    def __iter__(self):
        # Tell Task to resume me here.
        yield self
        return self.result

    def add_done_callback(self, fn):
        self._callbacks.append(fn)

    def set_result(self, result):
        self.result = result
        for fn in self._callbacks:
            fn(self)

class Task:
	'''
	传入生成Future的生成器，并且开始生成器的迭代
	'''
    def __init__(self, coro):
        self.coro = coro           #生成Future的生成器
        f = Future()
        f.set_result(None)
        self.step(f)

    def step(self, future):
        try:
            next_future = self.coro.send(future.result)
        except StopIteration:
            return

        next_future.add_done_callback(self.step)

class Fetcher:
	def fetch(self):
    	sock = socket.socket()
        sock.setblocking(False)
        try:
            sock.connect(('xkcd.com', 80))
        except BlockingIOError:
            pass

        f = Future()

        def on_connected():
            f.set_result(None)

        selector.register(sock.fileno(),EVENT_WRITE,on_connected)
        yield from f
        selector.unregister(sock.fileno())
        print('connected!')
        request = 'GET {} HTTP/1.0\r\nHost: www.cnblogs.com\r\n\r\n'.format(self.url)
        sock.send(request.encode('utf-8'))
        read_all(sock)



#每调用一次read方法读取4K的数据
def read(sock):
    f = Future()

    def on_readable():
        f.set_result(sock.recv(4096))#间接调用Task中step方法来终止生成器

    selector.register(sock.fileno(), EVENT_READ, on_readable)
    chunk = yield from f  # Read one chunk.
    selector.unregister(sock.fileno())
    return chunk

def read_all(sock):
    response = []
    # Read whole response.
    chunk = yield from read(sock)
    while chunk:
        response.append(chunk)
        chunk = yield from read(sock)

    return b''.join(response)




def loop():
    while not stopped:
        events = selector.select()
        for event_key, event_mask in events:
            callback = event_key.data
            callback(event_key, event_mask)


# Begin fetching http://xkcd.com/353/
fetcher = Fetcher('/353/')
Task(fetcher.fetch())

loop()