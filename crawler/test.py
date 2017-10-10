#coding:utf-8

import socket
import re

def fetch(url):
    sock = socket.socket()
    #sock.setblocking(False)
    sock.connect(('www.cnblogs.com', 80))
    #format方法被用于字符串的格式化输出,将format中的参数填充到{}中去，还可以使用序号
    #如{1}
    request = 'GET {} HTTP/1.0\r\nHost: www.cnblogs.com\r\n\r\n'.format(url)
    sock.send(request.encode('ascii'))
    response = b''
    chunk = sock.recv(4096)
    while chunk:
        response += chunk
        chunk = sock.recv(4096)
    print(response)
    content = re.split('\r\n\r\n',response.decode('utf-8'),1)[1]
    with open('test.html', 'w',encoding='utf-8') as f:
        f.write(content)

    # Page is now downloaded.
    #links = parse_links(response)
    #q.add(links)
#send方法调用次数与yield的函数的出现次数相同
#第一次调用时生成器从代码开始处开始，执行到第一个yield语句停止，
#并返回yield关键字后面的值作为生成器生成的对象,将传入的值复制给yield的返回值，如下面的result
#每次执行yield语句的地方生成器就停止向下执行，
#直到再一次调用send方法或者next方法才会继续向下执行
#yield from语句将后面语句的返回值复制给前面的表达式，直到后面的语句执行完成才会返回
def gen_fn():
    result = yield 1
    print('result of yield: {}'.format(result))
    result2 = yield 2
    print('result of 2nd yield: {}'.format(result2))
    return 'done'

def caller_fn():
    gen = gen_fn()
    rv = yield from gen
    print('return value of yield-from: {}'.format(rv))

caller = caller_fn()
print(caller.send(None))
print(caller.send('h'))
print(caller.send('b'))

#The generator flag is bit position 5.
generator_bit = 1 << 5
#When you call a generator function, Python sees the generator flag, 
#and it does not actually run the function. Instead, it creates a generator:
#每一次调用都返回的一个新的生成器，
gen = gen_fn()
print(gen.send(None))
print(gen.send('hello'))
print(bool(gen_fn.__code__.co_flags & generator_bit))
print ('b\'xxx\' is str?', isinstance(b'xxx', str))