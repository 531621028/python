# coding:utf-8
from lxml import etree
import requests


def getHtml(url):
    try:
        resp = requests.get(url, timeout=30)
        # 如果状态码不是200 则应发HTTOError异常
        resp.raise_for_status()
        # 设置正确的编码方式
        # resp.encoding = resp.apparent_encoding()
        resp.encoding = "utf-8"
        return resp.text
    except Exception as e:
        print(e)


def getContent(html):
    selector = etree.HTML(html)
    phs = selector.xpath("//div[@class='show-content']/p/text()")
    content = ''
    for ph in phs:
        content += ph
    return content


if __name__ == '__main__':
    url = "http://www.jianshu.com/p/6d96ac403100"
    html = getHtml(url)
    content = getContent(html)
    print(content)
