#由于Python是动态语言，根据类创建的实例可以任意绑定属性
#给实例绑定属性的方法是通过实例变量，或者通过self变量
class Student(object):
	def __init__(self,name):
		self.name = name
s = Student('hk')
s.score = 90
print(s.name)
print(s.score)
#如果Student类本身需要绑定一个属性呢？可以直接在class中定义属性，这种属性是类属性，归Student类所有
class Student(object):
	name = 'Student'
s = Student() # 创建实例s
print(s.name)
s.name = 'Michael' # 给实例绑定name属性
print(s.name) # 由于实例属性优先级比类属性高，因此，它会屏蔽掉类的name属性
del s.name # 如果删除实例的name属性
print(s.name) # 再次调用s.name，由于实例的name属性没有找到，类的name属性就显示出来了
