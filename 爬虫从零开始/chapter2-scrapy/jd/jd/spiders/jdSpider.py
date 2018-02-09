# coding:utf-8

import re
import datetime  # 引入datetime模块
from scrapy import Spider
from scrapy.http import Request
from jd.items import JdItem


def modifyStr(lines):
    '''
    将获取的文本中的换行去掉
    '''
    if type(lines) is list:
        results = []
        for line in lines:
            results.append(re.sub('\s', '', line))
        lines = ''.join(results)
    return lines


class jdSpider(Spider):
    name = 'jdSpider'
    start_urls = ['https://item.jd.com/2078473.html']
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
            request = Request(url=url, callback=self.parse_detail)
            request.meta['AJAX'] = True  # 是否使用AJAX获取数据
            yield request

    def parse(self, response):
        pass

    def parse_detail(self, response):
        item = JdItem()
        item['good_title'] = modifyStr(
            response.xpath('//div[@class="sku-name"]/text()')
            .extract())
        item['good_name'] = response.xpath(
            '//*[@id="detail"]/div[2]/div[1]/div[1]/ul[2]/li[1]/@title'
        ).extract_first()
        item['good_num'] = response.xpath(
            '//*[@id="detail"]/div[2]/div[1]/div[1]/ul[2]/li[2]/@title'
        ).extract_first()
        item['price'] = response.xpath(
            '/html/body/div[5]/div/div[2]/div[4]/div/div[1]/div[2]/span[1]/span[2]/text()'
        ).extract_first()
        item['shop_name'] = modifyStr(
            response.xpath('//*[@id="crumb-wrap"]/div/div[2]/div[1]/em/text()')
            .extract())
        item['comment_sum'] = response.xpath(
            '//*[@id="detail"]/div[1]/ul/li[5]/s/text()').extract_first()
        item['link'] = response.url
        item['date'] = str(
            datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        yield item