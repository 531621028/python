#写列表生成式时，把要生成的元素x * x放到前面，后面跟for循环
L=[x * x for x in range(1, 11)]
#for循环后面还可以加上if判断，这样我们就可以筛选出仅偶数的平方：
L=[x * x for x in range(1, 11) if x % 2 == 0]
print(L)
import os
L=[d for d in os.listdir('.')]
print(L)
d = {'x': 'A', 'y': 'B', 'z': 'C' }
L=[k + '=' + v for k, v in d.items()]
print(L)
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() for s in L1 if isinstance(s,str)]
print(L2)