# coding:utf-8
from scrapy.selector import Selector

# open函数默认打开当前目录的上一次目录
with open('chapter2-scrapy\demo.xml', 'r', encoding='utf-8') as f:
    body = f.read()
# print(Selector(text=body).xpath('/html/body/class[1]').extract())
# print(Selector(text=body).xpath('/html/body/class[last()]').extract())
# print(
#     Selector(text=body).xpath('/html/body/class[last()]/name/text()')
#     .extract())
subbody = Selector(text=body).xpath('/html/body/class[2]').extract()
print(subbody)
print(Selector(text=subbody[0]).xpath('//name/text()').extract())