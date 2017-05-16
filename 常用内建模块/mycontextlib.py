from contextlib import contextmanager

class Query(object):
	"""docstring for Query"""
	def __init__(self, name):
		super(Query, self).__init__()
		self.name = name
	def query(self):
		 print('Query info about %s...' % self.name)
@contextmanager
def create_query(name):
		print('Begin')
		q = Query(name)
		yield q
		print('End')
with create_query('Bob') as q:
    q.query()
#with语句首先执行yield之前的语句，因此打印出<h1>；
#yield调用会执行with语句内部的所有语句，因此打印出hello和world；
#最后执行yield之后的语句，打印出</h1>。
@contextmanager
def tag(name):
    print("<%s>" % name)
    yield
    print("</%s>" % name)

with tag("h1"):
    print("hello")
    print("world")

from contextlib import closing
from urllib.request import urlopen
with closing(urlopen('https://www.python.org')) as page:
	for line in page:
		print(line)

