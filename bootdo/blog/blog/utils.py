#coding:utf-8
import re


def getLinks(links=[]):
    pattern = 'href="(/|\w)+"'
    results = []
    for link in links:
        print(link)
        result = re.search(pattern, link)
        if result:
            results.append(result.group().split('=')[1][1:-1])
    return results

if __name__ =='__main__':
    link = r'<a class="title" target="_blank" href="/p/1d3f6cfff0ef">20180122领域建模讨论</a>'
    pattern = 'href="(/|\w)+"'
    result = re.search(pattern, link)
    print(result.group().split('=')[1][1:-1])
    