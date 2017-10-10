#coding:utf-8

import re
import socket
import selectors
import traceback

urls_todo = set(['/'])
seen_urls = set(['/'])

class Fetcher:
    def __init__(self, url):
        self.response = b''  # Empty array of bytes.
        self.url = url
        self.sock = None

    def fetch(self):
        self.sock = socket.socket()
        print(self.sock)
        #self.sock.setblocking(False)
        try:
            self.sock.connect(('www.cnblogs.com', 80))
            print(self.sock)
            #If zero is given, the socket is put in non-blocking mode(非租塞). 
            #If None is given, the socket is put in blocking mode(阻塞).
            #sock.setblocking(False) is equivalent to sock.settimeout(0.0) 
            print(self.sock.gettimeout())
            self.sock.setblocking(False)#起作用了
            print(self.sock.gettimeout())
            # Register next callback.
            print(self.sock.fileno())
            selector.register(self.sock.fileno(),selectors.EVENT_WRITE,self.connected)
        except BlockingIOError:
            print('ERROR')



    # Method on Fetcher class.

    def connected(self, key, mask):
        print('connected!')
        #fd:Underlying file descriptor(底层文件描述符).
        selector.unregister(key.fd)
        request = 'GET {} HTTP/1.0\r\nHost: www.cnblogs.com\r\n\r\n'.format(self.url)
        self.sock.send(request.encode('ascii'))

        # Register the next callback.
        selector.register(key.fd,
                          selectors.EVENT_READ,
                          self.read_response)

    # Method on Fetcher class.
    def read_response(self, key, mask):
        global stopped

        chunk = self.sock.recv(4096)  # 4k chunk size.
        if chunk:
            self.response += chunk
        else:
            selector.unregister(key.fd)  # Done reading.
            print('read_response')
            #print(self.response.decode('utf-8'))
            #links = self.parse_links()

            # Python set-logic:
            #for link in links.difference(seen_urls):
            #    urls_todo.add(link)
            #    Fetcher(link).fetch()  # <- New Fetcher.

            #seen_urls.update(links)
            #urls_todo.remove(self.url)
            #if not urls_todo:
            #    stopped = True
            stopped = True

selector = selectors.DefaultSelector()
fetcher = Fetcher('/Alexzzzz/p/6832253.html')
fetcher.fetch()

stopped = False

def loop():
    while not stopped:
        events = selector.select()
        for event_key, event_mask in events:
            callback = event_key.data
            callback(event_key, event_mask)
loop()