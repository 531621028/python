#sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序，例如按绝对值大小排序：
#key指定的函数将作用于list的每一个元素上，并根据key函数返回的结果进行排序。
#对比原始的list和经过key=abs处理过的list：
print(sorted([36, 5, -12, 9, -21], key=abs))
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower))
#要进行反向排序，不必改动key函数，可以传入第三个参数reverse=True
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower,reverse=True))
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def byName(t):
	return t[0]
L2 = sorted(L,key=byName)
print(L2)

def byName(t):
	return t[1]
L3 = sorted(L,key=byName)
print(L3)