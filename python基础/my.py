print("包含中文的str")
print(ord("A"))
print(ord("中"))
print(chr(21318))
print('\u4e2d\u6587')
x=b"abd"
print("ABC".encode('ascii'))
print("中文".encode('utf-8'))
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))
#len()函数计算的是str的字符数，如果换成bytes，len()函数就计算字节数：
print(len("中文"))
print('Hello, %s' % 'world')
print('Hi, %s, you have $%d.' % ('Michael', 1000000))