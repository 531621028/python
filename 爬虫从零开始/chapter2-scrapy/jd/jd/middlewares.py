# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html
import time
from scrapy import signals
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from scrapy.http import HtmlResponse


class JdMiddleware(object):
    def __init__(self):
        self.driver = webdriver.PhantomJS()
        print('************JDMiddleware Init************')

    # 当每个request通过下载中间件时，该方法被调用
    def process_request(self, request, spider):
        print('----------download middleware process_request execuate--------')
        if 'AJAX' in request.meta:  # 如果网站使用AJAX则使用PhantomJS执行
            self.driver.get(request.url)
            # 查找元素并点击
            # self.driver.find_element_by_xpath('//*[@id="detail"]/div[1]/ul/li[5]').click()
            # WebDriverWait(self.driver, 20, 0.5).until(
            #     EC.presence_of_element_located(
            #         (By.XPATH,
            #          '//div[@id="comment"]/div[2]/div[1]/div[2]')))

            content = self.driver.page_source.encode('utf-8')
            # 这只返回的编码为utf-8
            return HtmlResponse(
                request.url, body=content, request=request, encoding='utf-8')

    # 当每个request通过下载中间件时，该方法被调用
    def process_response(self, request, response, spider):
        print('----------download middleware process_response execuate-------')
        return response

    def __del__(self):
        self.driver.quit()
        print('************JDMiddleware Destroy************')


class JdSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
