#我们来判断对象类型，使用type()函数
print(type(123))
print(type('a'))
print(type(abs))
#如果要判断一个对象是否是函数怎么办？可以使用types模块中定义的常量：
import types
def fn():
	pass
print(type(fn) == types.FunctionType)
#对于class的继承关系来说，可以使用isinstance()函数
#如果要获得一个对象的所有属性和方法，可以使用dir()函数
print(dir('abv'))
#配合getattr()、setattr()以及hasattr()，我们可以直接操作一个对象的状态
class MyObject(object):
	def __init__(self):
		self.x = 9
	def power():
		return self.x * self.x
obj = MyObject()
print(hasattr(obj,'x'))
setattr(obj,'y',19)
print(getattr(obj,'y'))

