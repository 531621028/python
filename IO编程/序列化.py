import pickle
d = dict(name='Bob', age=20, score=88)
#pickle.dumps()方法把任意对象序列化成一个bytes，
#然后，就可以把这个bytes写入文件。
#或者用另一个方法pickle.dump()直接把对象序列化后写入一个file-like Object：
print(pickle.dumps(d))
with open('dump.txt','wb') as f:
	pickle.dump(d,f)
d = 0
with open('dump.txt','rb') as f:
	d = pickle.load(f)
print(d)
import json
#dumps()方法返回一个str，内容就是标准的JSON。
#类似的，dump()方法可以直接把JSON写入一个file-like Object
d = dict(name='Bob', age=20, score=88)
print(json.dumps(d))

class Student(object):
	def __init__(self, name, age, score):
		self.name = name
		self.age = age
		self.score = score
	def student2dict(std):
		return {
			'name': std.name,
			'age': std.age,
			'score': std.score
		}
s = Student('Bob', 20, 88)
#因为通常class的实例都有一个__dict__属性，
#它就是一个dict，用来存储实例变量。也有少数例外，比如定义了__slots__的class
print(json.dumps(s, default=lambda obj: obj.__dict__))