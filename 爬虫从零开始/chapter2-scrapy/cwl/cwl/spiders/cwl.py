# coding:utf-8
from scrapy import Spider
from scrapy.selector import Selector
from scrapy.http import Request
from cwl.items import CwlItem
from scrapy.settings import Settings


class cwl(Spider):
    name = 'cwl'
    start_urls = ['http://www.cwl.gov.cn/kjxx/ssq/kjgg/']
    custom_settings = {
        'HOST': 'localhost',
        'PORT': 3306,
        'USERNAME': 'root',
        'PASSWORD': 'root',
        'DBNAME': 'cwl',
        'ITEM_PIPELINES': {'cwl.pipelines.CwlPipeline': 300}
    }

    # 重写第一次请求处理函数，要返回Request对象
    def start_requests(self):
        url = cwl.start_urls[0]
        request = Request(url=url, callback=self.parse)
        request.meta['AJAX'] = True # 是否使用AJAX获取数据
        yield request

    def parse(self, response):
        # xpath返回的是一个list
        recordList = response.xpath('//div[@class="bgzt"]/table/tbody/tr').extract()
        for record in recordList:
            item = CwlItem()
            ss = Selector(text=record)
            item['qiHao'] = ss.xpath('//td[1]/text()').extract()[0]
            nums = []
            for num in ss.xpath('//td[3]/span/text()').extract():
                nums.append(num)
            nums.append(ss.xpath('//td[4]/span/text()').extract()[0])
            item['nums'] = nums
            yield item




