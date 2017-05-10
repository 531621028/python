#如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__，在Python中，
#实例的变量名如果以__开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问
class Student(object):
	"""docstring for Student"""
	def __init__(self, name,score):
		self.__name = name
		self.__score = score
	def print_score(self):
		print('%s: %s' % (self.__name, self.__score))
	def get_name(self):
		return self.__name
	def get_score(self):
		return self.__score
bart = Student('Bart Simpson', 98)
bart.print_score()

bart.__name = 'New Name'
print(bart.__name)
#表面上看，外部代码“成功”地设置了__name变量，
#但实际上这个__name变量和class内部的__name变量不是一个变量！
#内部的__name变量已经被Python解释器自动改成了_Student__name，
#而外部代码给bart新增了一个__name变量。不信试试：
print(bart.get_name())
