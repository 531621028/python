# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field
from sqlalchemy import Column, String, create_engine


class JdItem(Item):
    good_num = Field()  # '商品编号'
    good_title = Field()     # '商品标题'
    good_name = Field()       # '商品名称'
    price = Field()      # '商品价格'
    comment_sum = Field()   # '商品评论总数'
    shop_name = Field()  # '店铺名称'
    link = Field()   # '商品链接'
    date = Field()   # '爬取日期'
