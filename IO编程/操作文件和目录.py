import os
print(os.name)
print(os.environ)
print(os.environ.get('PATH'))
print(os.path.abspath('.'))
path = os.path.join(os.path.abspath('.'),'testdir')
print(path)
os.mkdir(path)
os.rmdir(path)
file = os.path.split(os.path.abspath('.')+'文件读写.py')
print(file)
str1 = 'a'+'b'
print(str1)
print([x for x in os.listdir('../') if os.path.isdir(x)])
print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py'])
print(os.listdir('.'))

