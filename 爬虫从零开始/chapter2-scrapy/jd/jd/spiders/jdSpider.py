# coding:utf-8
from scrapy import Spider
from scrapy.selector import Selector
from scrapy.http import Request
from jd.items import JdItem
import re


class jdSpider(Spider):
    name = 'jdSpider'
    start_urls = ['https://item.jd.com/526825.html']
    base_url = 'https://www.jd.com/'
    custom_settings = {
        'HOST': 'localhost',
        'PORT': 3306,
        'USERNAME': 'root',
        'PASSWORD': 'root',
        'DBNAME': 'cwl',
        'ITEM_PIPELINES': {
            'jd.pipelines.JdPipeline': 300
        },
        'DOWNLOADER_MIDDLEWARES': {
            'jd.middlewares.JdMiddleware': 300
        }
    }

    # 重写第一次请求处理函数，要返回Request对象
    def start_requests(self):
        for url in jdSpider.start_urls:
            request = Request(url=url, callback=self.parse)
            request.meta['AJAX'] = True  # 是否使用AJAX获取数据
            yield request

    def parse(self, response):
        pass

    def parse_detail(self, response):
        pass