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
#如果传入列表参数,Beautiful Soup会将与列表中任一元素匹配的内容返回.下面代码找到文档中所有<a>标签和<b>标签
#如果传入正则表达式作为参数,Beautiful Soup会通过正则表达式的 match() 来匹配内容.
#True 可以匹配任何值,下面代码查找到所有的tag,但是不会返回字符串节点
#如果没有合适过滤器,那么还可以定义一个方法,方法只接受一个元素参数,如果这个方法返回True 表示当前元素匹配并且被找到,如果不是则反回False

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
#find_all()方法中的参数都是默认参数
data_soup = BeautifulSoup('<div data-foo="value">foo!</div>')
print(data_soup.find_all('div',attrs={"data-foo": "value"}))

#按CSS搜索 class_ 参数同样接受不同类型的 过滤器 ,字符串,正则表达式,方法或 True :
print(soup.find_all("a", class_="sister"))

#text 参数通过 text 参数可以搜搜文档中的字符串内容.
#与name参数的可选值一样,text 参数接受字符串,正则表达式,列表,True.看例子:


link = soup.a
print(type(link))
print(type(link.next_sibling))
print(link.next_sibling.next_sibling)











