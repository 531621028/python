d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
   print(key)
   print(d[key])
from collections import Iterable
print(isinstance('abc',Iterable))
for i,value in enumerate(['a','b','c']):
	print(i,value)
for x, y in [(1, 1), (2, 4), (3, 9)]:
	print(x,y)