# coding:utf-8

import requests
import time
from bs4 import BeautifulSoup


# 首先我们写好抓取网页的函数
def get_html(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        # 这里我们知道百度贴吧的编码是utf-8，所以手动设置的。爬去其他的页面时建议使用：
        # r.endcodding = r.apparent_endconding
        r.encoding = 'utf-8'
        return r.text
    except Exception as e:
        print("获取失败，链接或网络有问题:", e)
        return "ERROR"


def get_book_info_list(url):
    '''
    爬取每一类型小说排行榜，
    按顺序写入文件，
    文件内容为 小说名字+小说链接
    将内容保存到列表
    并且返回一个装满url链接的列表
    '''
    html = get_html(url)
    soup = BeautifulSoup(html, 'lxml')
    main_div = soup.find('div', attrs={'id': 'main'})
    book_list_type = []
    for div in main_div.children:
        if div.name == 'div':
            type_list = {}
            name = div.find('div', class_='toptab').span.string
            type_list['name'] = name
            # with open('novel_list.csv', 'a+', encoding='utf-8') as f:
            #     f.write("\n小说种类：{} \n".format(name))
            # 我们直接通过style属性来定位总排行榜
            book_rank_div = div.find(style='display: block;')
            # 找到全部的小说名字，发现他们全部都包含在li标签之中
            book_rank_list = book_rank_div.find_all('li')
            book_list = []
            for book_info in book_rank_list:
                book = {}
                book['link'] = 'http://www.qu.la/' + book_info.a['href']
                book['title'] = book_info.a['title']
                book['rank'] = book_info.find('span', class_='num').text[-1:]
                book_list.append(book)
                # 这里使用a模式，防止清空文件
                # with open('novel_list.csv', 'a', encoding='utf-8') as f:
                #     f.write("小说名：{:<} \t 小说地址：{:<} \n".format(
                #         book['title'], book['link']))
            type_list['book_list'] = book_list
            book_list_type.append(type_list)
    return book_list_type


def get_book_content_list(book):
    book_chapter_url_list = []
    html = get_html(book['link'])
    soup = BeautifulSoup(html, 'lxml')
    chapters = soup.find_all('dd')
    print("{}的总章节数是{}".format(book['title'], len(chapters)))
    for chapter in chapters:
        book_chapter_url_list.append('http://www.qu.la/' + chapter.a['href'])
    return book_chapter_url_list


def main():
    url = 'http://www.qu.la/paihangbang/'
    for book_type in get_book_info_list(url)[0:1]:
        for book in book_type['book_list']:
            get_book_content_list(book)
        print('{}类型的小说已经完成'.format(book_type['name']))


if __name__ == '__main__':
    main()