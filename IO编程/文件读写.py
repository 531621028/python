#调用read()会一次性读取文件的全部内容，如果文件有10G，内存就爆了，
#所以，要保险起见，可以反复调用read(size)方法，每次最多读取size个字节的内容。
#另外，调用readline()可以每次读取一行内容，调用readlines()一次读取所有内容并按行返回list
with open('E:/Python/模块/使用模块.py',encoding='utf-8') as f:
	print(f.read())
#二进制文件
with open('E:/Python/模块/test.png','rb') as f:
	print(f.read())

with open('test.txt', 'w') as f:
    f.write('Hello, world!')