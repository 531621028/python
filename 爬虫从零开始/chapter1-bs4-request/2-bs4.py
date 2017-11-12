# coding:utf-8

# 导入bs4模块
from bs4 import BeautifulSoup
html ='''
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
</html>
'''
# 做一个美味汤
soup = BeautifulSoup(html, 'lxml')
# 输出结果
print(soup.find('body').text)
#print(soup.prettify())
