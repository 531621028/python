# coding:utf-8
from scrapy import Spider
from scrapy.selector import Selector
from scrapy.http import Request
from cwl.items import CwlItem
from scrapy.settings import Settings


class zhcw(Spider):
    name = 'zhcw'
    start_urls = ['http://www.zhcw.com/ssq/kjgg/']
    custom_settings = {
        'HOST': 'localhost',
        'PORT': 3306,
        'USERNAME': 'root',
        'PASSWORD': 'root',
        'DBNAME': 'cwl'
    }

    # 重写第一次请求处理函数，要返回Request对象
    def start_requests(self):
        url = zhcw.start_urls[0]
        request = Request(url=url, callback=self.parse)
        request.meta['AJAX'] = True # 是否使用AJAX获取数据
        yield request

    def parse(self, response):
        if(response.url.endswith('html')):
            print('记录')
        else:
            print('公告')
