# coding:utf-8
from scrapy.spider import Spider
from scrapy.http import Request
from blog.items import BlogItem
import re


class JianShuSpider(Spider):
    name = 'jianshu'
    start_urls = ['https://www.jianshu.com/c/5832399d3160']
    # start_urls = ['https://www.jianshu.com/p/1d3f6cfff0ef']

    # 重写第一次请求处理函数，要返回Request对象
    def start_requests(self):
        url = JianShuSpider.start_urls[0]
        tFlage = url.split("/")[-2]
        request = Request(url=url, callback=self.parse)
        if 'p' == tFlage:
            request.meta['JS'] = True
        yield request

    def parse(self, response):
        item = BlogItem()
        tFlage = response.url.split("/")[-2]
        if 'c' == tFlage:
            # @href获取a标签的href属性 a[@class="title"] 查找class为title的标签a
            urls = response.xpath('//div/a[@class="title"]/@href').extract()  
            for url in urls:  
                url = "https://www.jianshu.com" + url
                request = Request(url=url, callback=self.parse)
                request.meta['JS'] = True
                yield request
        else:
            article = response.xpath('//div[@class="article"]')
            item['article_name'] = article.xpath('//h1[@class="title"]/text()').extract()[0]
            item['article_url'] = response.url
            item['article_read'] = article.xpath('//span[@class="views-count"]/text()').extract()[0]
            item['article_author'] = article.xpath('//div[@class="info"]/span[@class="name"]/a/text()').extract()[0]
            item['article_ctime'] = article.xpath('//span[@class="publish-time"]/text()').extract()[0]
            item['article_slug'] = article.xpath('//div[@class="show-content"]//p/strong/text()').extract()[0].split(':')[1]
            item['article_content'] = self.getContentText(article.xpath('//div[@class="show-content"]//text()').extract())
            yield item

    def getContentText(self, lines):
        results = []
        for line in lines:
            line = re.sub(r'\W+', '', line)
            if line != '':
                results.append(line)
        return '\n'.join(results)

