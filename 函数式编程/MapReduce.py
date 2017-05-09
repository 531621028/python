#map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。
def f(x):
	return x * x
r = map(f,[1, 2, 3, 4, 5, 6, 7, 8, 9])
print(list(r))
print(r)
print(list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])))
#reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
from functools import reduce
def add(x,y):
	return x + y
print(reduce(add,[1,3,5,7,9]))
def fn(x,y):
	return x * 10 + y
print(reduce(fn,[1,3,5,7,9]))

def str2int(s):
	def fn(x,y):
		return x * 10 + y
	def char2num(s):
		return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
	return reduce(fn,map(char2num,s))
s = ['1','3','5','7','9']
print(str2int(s))

def normalize(name):
	return name[0].upper() + name[1:].lower()
L1 = ['adam', 'LISA', 'barT']
print('adam'[1:].lower())
L2 = list(map(normalize, L1))
print(L2)

def prod(L):
	def f(x,y):
		return x * y
	return reduce(f,L)
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
def char2num(s):
	return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
def str2int_(s):
	return reduce(lambda x,y : x*10+y,map(char2num,s))
def str2float_(s):
    return reduce(lambda x,y:x/10+y,map(char2num, s[::-1]))/10
def str2float(s):
    dot_index=s.find('.')
    if dot_index!= -1:
        return str2int_(s[:dot_index]) + str2float_(s[dot_index+1:])
    else:
        return str2int_(s)
print('str2float(\'123.456\') =', str2float('123.456'))