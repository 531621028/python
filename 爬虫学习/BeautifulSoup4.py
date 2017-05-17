html_doc = '''
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
'''
import re
from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc)
#参数可以查找所有名字为 name 的tag,字符串对象会被自动忽略掉
#搜索 name 参数的值可以使任一类型的 过滤器 ,字符窜,正则表达式,列表,方法或是 True
print(soup.find_all("title"))
#keyword 参数如果一个指定名字的参数不是搜索内置的参数名,
#搜索时会把该参数当作指定名字tag的属性来搜索,如果包含一个名字为 id 的参数,Beautiful Soup会搜索每个tag的”id”属性.
print(soup.find_all(id='link2'))
#搜索指定名字的属性时可以使用的参数值包括 字符串 , 正则表达式 , 列表, True .
print(soup.find_all(href=re.compile("elsie")))
#下面的例子在文档树中查找所有包含 id 属性的tag,无论 id 的值是什么:
print(soup.find_all(id=True))

data_soup = BeautifulSoup('<div data-foo="value">foo!</div>')
print(data_soup.find_all('div',attrs={"data-foo": "value"}))














