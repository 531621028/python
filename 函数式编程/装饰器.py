#由于函数也是一个对象，而且函数对象可以被赋值给变量，所以，通过变量也能调用该函数。
def now():
	print('2015-3-25')
	return 0
f = now
print(f())
#函数对象有一个__name__属性，可以拿到函数的名字
print(now.__name__)
#在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）
def log(func):
	def wrapper(*args,**kw):
		print('call %s():'% func.__name__)
		return func(*args,**kw)
	return wrapper
#把@log放到now()函数的定义处，相当于执行了语句：now = log(now)
@log
def now():
	print('2015-3-25')
	return 2017
print(now())

def log(text):
	def decorator(func):
		def wrapper(*args,**kw):
			print('%s %s():'%(text,func.__name__))
			return func(*args,**kw)
		return wrapper
	return decorator
@log('execute')
def now():
	print('2017-3-25')
now()
#和两层嵌套的decorator相比，3层嵌套的效果是这样的：now = log('execute')(now)
print(now.__name__)

#需要把原始函数的__name__等属性复制到wrapper()函数中，否则，有些依赖函数签名的代码执行就会出错。
#不需要编写wrapper.__name__ = func.__name__这样的代码，
#Python内置的functools.wraps就是干这个事的，所以，一个完整的decorator的写法如下：
import functools

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper
@log
def now():
	print('2017-3-25')
print(now.__name__)


def log(text):
	if isinstance(text,str):
		def decorator(func):
			@functools.wraps(func)
			def wrapper(*args,**kw):
				print('%s %s():'%(text,func.__name__))
				return func(*args,**kw)
			return wrapper
		return decorator
	else:
		@functools.wraps(text)
		def wrapper(*args,**kw):
			print('call %s():'%(text.__name__))
			return text(*args,**kw)
		return wrapper

@log
def now():
	print('2017-3-25')
now()
@log('execute')
def now():
	print('2017-3-25')
now()