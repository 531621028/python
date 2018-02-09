# coding:utf-8
from scrapy import Spider
from scrapy.selector import Selector
from scrapy.http import Request
from cwl.items import CwlItem
import re


def isGongGao(url):
    '''
    判断页面是记录页面还是公告页面
    '''
    try:
        page = url.split('/')[-1]
        if re.match(r'\d+\.shtml', page):
            return False  # 记录页面返回False
    except Exception as e:
        print(e)
    return True


def getQiHao(line):
    return re.search('\d+', ''.join(line)).group()


class zhcw(Spider):
    urlDict = {}
    name = 'zhcw'
    start_urls = ['http://www.zhcw.com/ssq/kjgg']
    base_url = 'http://www.zhcw.com'
    custom_settings = {
        'HOST': 'localhost',
        'PORT': 3306,
        'USERNAME': 'root',
        'PASSWORD': 'root',
        'DBNAME': 'cwl',
        'ITEM_PIPELINES': {
            'cwl.pipelines.CwlPipeline': 300
        },
        'DOWNLOADER_MIDDLEWARES': {
            'cwl.middlewares.ZhcwMiddleware': 300
        }
    }

    # 重写第一次请求处理函数，要返回Request对象
    def start_requests(self):
        url = zhcw.start_urls[0]
        request = Request(url=url, callback=self.parse)
        request.meta['AJAX'] = True  # 是否使用AJAX获取数据
        yield request

    def parse(self, response):
        if not isGongGao(response.url):
            print('--------------记录页面---------------', response.url)
            try:
                item = CwlItem()
                item['qiHao'] = getQiHao(
                    response.xpath('//h1[@class="bt"]//text()').extract())
                item['nums'] = response.xpath(
                    '//div[@class="winning_ball"]/table/tbody/tr/td[1]/span/text()'
                ).extract()
                item['nums'].append(
                    response.xpath(
                        '//div[@class="winning_ball"]/table/tbody/tr/td[2]/span/text()'
                    ).extract_first())
                yield item
            except:
                if response.url not in zhcw.urlDict:
                    zhcw.urlDict[response.url] = 1
                else:
                    if zhcw.urlDict[response.url] < 5:
                        zhcw.urlDict[response.url] += 1
                        print('--没有获取到数据{0}重新获取--'.format(
                            zhcw.urlDict[response.url]))
                        request = Request(response.url, callback=self.parse)
                        request.meta['AJAX'] = True  # 是否使用AJAX获取数据
                        yield request
        else:
            print('--------------公告页面---------------', response.url)
            try:
                urls = response.xpath(
                    '//ul[@class="Hlistul"]/li/span[@class="Nlink"]/a/@href'
                ).extract()
                next_page_url = '/ssq/kjgg/' + response.xpath(
                    '//*[@id="ssq_main"]/div[1]/div/div/table/tbody/tr/td/a/@href'
                ).extract()[-2]
                urls.append(next_page_url)
                # print(urls)
                for url in urls:
                    request = Request(zhcw.base_url + url, callback=self.parse)
                    request.meta['AJAX'] = True  # 是否使用AJAX获取数据
                    yield request
            except:
                print('没有找到记录或页面')
