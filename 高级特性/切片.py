L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
print(L[0:3])
#记住倒数第一个元素的索引是-1
print(L[-2:])
L = list(range(100))
print(L)
#前10个数，每两个取一个
print(L[:10:2])
print(L[::5])
print(L[:])
#字符串'xxx'也可以看成是一种list
print('ABCDEFG'[:3])