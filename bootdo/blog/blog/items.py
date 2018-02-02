# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class BlogItem(Item):
    article_name = Field()
    article_url = Field()
    article_author = Field()
    article_ctime = Field()
    article_slug = Field()
    article_content = Field()
    article_read = Field()
