import selectors  #基于select模块实现的IO多路复用，建议大家使用
import socket
sock=socket.socket()
sock.bind(('127.0.0.1',8800))
sock.listen(5)
sock.setblocking(False)
sel=selectors.DefaultSelector() #根据平台选择最佳的IO多路机制，比如linux就会选择epoll

def read(conn,mask):
    try:
        data=conn.recv(1024)
        print(data.decode('utf8'))
        data2=input('>>>>')
        conn.send(data2.encode('utf8'))
    except Exception:
        sel.unregister(conn)

def accept(sock,mask):
    conn,addr=sock.accept()
    print('-------',conn)
    sel.register(conn,selectors.EVENT_READ,read)
sel.register(sock, selectors.EVENT_READ, accept)  #注册功能
while True:
    print('wating....')
    events=sel.select()   #[(sock)，（），（）]   监听

    for key,mask in events:
        # print(key.data)       #accept   找出有活动的绑定函数
        # print(key.fileobj)    #sock     找出有活动的文件描述符

        func=key.data
        obj=key.fileobj

        func(obj,mask)  #1 accept(sock,mask) 2read(conn,mask)
客户端
import socket
tin=socket.socket()
tin.connect(('127.0.0.1',8800))
while True:
    inp=input('>>>>')
    tin.send(inp.encode('utf8'))
    data=tin.recv(1024)
    print(data.decode('utf8'))