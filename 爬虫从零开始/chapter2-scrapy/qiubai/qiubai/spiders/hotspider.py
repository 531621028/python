# -*- coding: utf-8 -*-
import scrapy


class HotspiderSpider(scrapy.Spider):
    name = 'hotspider'
    allowed_domains = ['qiushibaike.com']
    start_urls = ['http://qiushibaike.com/']

    def parse(self, response):
        pass
