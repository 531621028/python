#只要把一个列表生成式的[]改成()，就创建了一个generator
g = (x * x for x in range(10))
print(next(g))
#如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator
def fib(max):
	n,a,b = 0,0,1
	while n < max:
		yield b
		a,b = b,a + b
		n += 1
	return 'done'
print(fib(6))

def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield(3)
    print('step 3')
    yield(5)
o = odd()
print(next(o))
print(next(o))
g = fib(6)
while True:
	try:
		x = next(g)
		print('g',x)
	except Exception as e:
		print('Generator return value:', e.value)
		break
#杨辉三角
def triangles():
	L=[1]
	while True:
		yield L
		#L长度为0或1的时候不执行生成表达式
		L=[1]+[L[i]+L[i+1] for i in range(0,len(L)-1)]+[1]
n = 0
for t in triangles():
	print(t)
	n += 1
	if n == 10:
		break
L = range(0,100)
print(L)