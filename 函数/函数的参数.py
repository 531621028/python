def power(x,n = 2):
	s = 1
	while n > 0:
		n = n - 1
		s = s * x
	return s
print(power(5))
def enroll(name, gender, age=6, city='Beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)

#可变参数,可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
print(calc(1,2,3,4,5))
print(calc())
#使用*args和**kw是Python的习惯写法，当然也可以用其他参数名，但最好使用习惯用法。
#关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict
def person(name, age, **kww):
    print('name:', name, 'age:', age, 'other:', kww)
person('Michael', 30)
person('Bob', 35, city='Beijing')
#**extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数
# kw将获得一个dict，注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra
extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, **extra)

#和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数
def person(name, age, *, city, job):
    print(name, age, city, job)
#如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了：
def person(name, age, *arg, city, job):
    print(name, age, args, city, job)
#命名关键字参数必须传入参数名，这和位置参数不同，name为位置参数
def person(name, age, *, city='Beijing', job):
    print(name, age, city, job)
person('Jack', 24, job='Engineer')

def person(name, age, *arg, job):
    print(name, age, arg, job)
person('Jack', 28,job='Engineer')






#总结
#默认参数在调用的时候可以传入k=2,或者直接传入2