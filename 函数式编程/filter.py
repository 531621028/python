#和map()类似，filter()也接收一个函数和一个序列。和map()不同的是，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素
def is_odd(x):
	return x % 2 == 1
print(list(filter(is_odd,[1,2,3,4,5,6,7,8,9])))
#注意到filter()函数返回的是一个Iterator，也就是一个惰性序列，所以要强迫filter()完成计算结果，需要用list()函数获得所有结果并返回list

def _odd_iter():
	n = 1
	while True:
		n = n + 2
		yield n
def _not_divisible(n):
	return lambda x : x % n > 0
def primes():
	yield 2
	it = _odd_iter()
	while True:
		n = next(it)
		yield n
		it = filter(_not_divisible(n),it)
for n in primes():
    if n < 1000:
    	pass
    else:
        break
def is_palindrome(n):
	y = n
	sum = 0
	while y != 0:
		x = y % 10
		y = int(y / 10)
		sum = sum * 10 + x
	return sum == n
output = filter(is_palindrome, range(1, 1000))
print(list(output))