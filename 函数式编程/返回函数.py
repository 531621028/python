#高阶函数除了可以接受函数作为参数外，还可以把函数作为结果值返回
def lazy_sum(*args):
	def sum():
		ax = 0
		for n in args:
			ax += n
		return ax
	return sum
f = lazy_sum(1,3,5,7,9)
print(f)
#另一个需要注意的问题是，返回的函数并没有立刻执行，而是直到调用了f()才执行
print(f())
#当我们调用lazy_sum()时，每次调用都会返回一个新的函数，即使传入相同的参数：
f1 = lazy_sum(1, 3, 5, 7, 9)
f2 = lazy_sum(1, 3, 5, 7, 9)
print(f1 == f2)
#返回闭包时牢记的一点就是：返回函数不要引用任何循环变量，或者后续会发生变化的变量。
def count():
	fs = []
	for i in range(1,4):
		def f():
			return i * i
		fs.append(f)
	return fs
f1,f2,f3 = count()
print(f1())
print(f2())
print(f3())
#如果一定要引用循环变量怎么办？方法是再创建一个函数，用该函数的参数绑定循环变量当前的值，无论该循环变量后续如何更改，已绑定到函数参数的值不变：
def count():
	def f(j):
		def g():
			return j * j
		return g
	fs = []
	for i in range(1,4):
		fs.append(f(i))
	return fs
f1,f2,f3 = count()
print(f1())
print(f2())
print(f3())
