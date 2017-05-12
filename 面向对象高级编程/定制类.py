#__str__相当于Java的toString()方法
class Student(object):
	def __init__(self,name):
		self.name = name
	def __str__(self):
		return 'Student object(name:%s)'% self.name
print(Student('Michael'))
#__iter__为迭代使用
class Fib(object):
	def __init__(self):
		self.a,self.b = 0,1 # 初始化两个计数器a，b
	def __iter__(self):
		return self # 实例本身就是迭代对象，故返回自己
	def __next__(self):
		self.a, self.b = self.b, self.a + self.b # 计算下一个值
		if self.a > 100000: # 退出循环的条件
			raise StopIteration()
		return self.a # 返回下一个值
for n in Fib():
	print(n)
#__getitem__像python中的list一样使用[1,2][0]
class Fib(object):
	def __getitem__(self, n):
		if isinstance(n, int): # n是索引
			a, b = 1, 1
			for x in range(n):
				a, b = b, a + b
			return a
		if isinstance(n, slice): # n是切片
			start = n.start
			stop = n.stop
			if start is None:
				start = 0
			a, b = 1, 1
			L = []
			for x in range(stop):
				if x >= start:
					L.append(a)
				a, b = b, a + b
			return L
f = Fib()
print(f[:10:2])
#当调用不存在的属性时，Python解释器会试图调用__getattr__(self, 'score')来尝试获得属性，
#只需要定义一个__call__()方法，就可以直接对实例进行调用
class Student(object):
	def __init__(self, name):
		self.name = name
	def __call__(self):
		print('My name is %s.' % self.name)
s = Student('Michael')
s()
#通过callable()函数，我们就可以判断一个对象是否是“可调用”对象
print(callable(Student('1')))
print(callable([1, 2, 3]))
