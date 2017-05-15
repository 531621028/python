try:
	print('try')
	r = 10 / 0
except ZeroDivisionError as e:
	print('except:',e)
finally:
	print('finally')
print('END')

#使用try...except捕获错误还有一个巨大的好处，就是可以跨越多层调用，比如函数main()调用foo()，foo()调用bar()，结果bar()出错了，这时，只要main()捕获到了，就可以处理：
def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except Exception as e:
        print('Error:', e)
    finally:
        print('finally...')

import logging
def foo(s):
	return 10 / int(s)
def bar(s):
	return foo(s) * 2

def main():
	try:
		bar('0')
	except Exception as e:
		logging.exception(e)
main()
print('END')

class FooError(ValueError):
	pass
def foo(s):
	n = int(s)
	if n == 0:
		raise FooError('invalid value:%s'% s)
	return 10 / n
foo('0')