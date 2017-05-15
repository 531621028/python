from collections import namedtuple
#namedtuple是一个函数，它用来创建一个自定义的tuple对象，并且规定了tuple元素的个数，并可以用属性而不是索引来引用tuple的某个元素
Point = namedtuple('Point', ['x', 'y'])
p = Point(1,2)
print(p.x)
print(p.y)
Circle = namedtuple('Circle',['x','y','r'])
c = Circle(1,2,3)
print(c.x)
#deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈
from collections import deque
q = deque(['a','b','c'])
q.append('x')
q.appendleft('y')
print(q)
#使用dict时，如果引用的Key不存在，就会抛出KeyError。如果希望key不存在时，返回一个默认值，就可以用defaultdict
from collections import defaultdict
dd = defaultdict(lambda:'N/A')
dd['key1'] = 'abc'
print(dd['key1'])
print(dd['key2'])
#使用dict时，Key是无序的。在对dict做迭代时，我们无法确定Key的顺序。
#如果要保持Key的顺序，可以用OrderedDict
from collections import OrderedDict
d = dict([('a',1),('b',2),('c',3)])
print(d)
#注意，OrderedDict的Key会按照插入的顺序排列，不是Key本身排序
od = OrderedDict([('a',1),('b',2),('c',3)])
print(od)
#Counter是一个简单的计数器
from collections import Counter
c = Counter()
for ch in 'programming':
	c[ch] = c[ch] + 1
print(c)
