#class后面紧接着是类名，即Student，类名通常是大写开头的单词，紧接着是(object)，表示该类是从哪个类继承下来的
#注意到__init__方法的第一个参数永远是self，表示创建的实例本身
#因此，在__init__方法内部，就可以把各种属性绑定到self，因为self就指向创建的实例本身。
class Student(object):
	"""docstring for Student"""
	def __init__(self, arg):
		super(Student, self).__init__()
		self.arg = arg
		
bart = Student('hk')
print(bart)
#可以自由地给一个实例变量绑定属性，比如，给实例bart绑定一个name属性
bart.name = 'bart simpson'
print(bart.name)

class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))
bart = Student('Bart Simpson', 59)
bart.print_score()
