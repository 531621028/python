# coding:utf-8

import requests
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
    except:
        return " ERROR "


def print_result(url):
    '''
    查询比赛结果，并格式化输出！
    '''
    html = get_html(url)
    soup = BeautifulSoup(html, 'lxml')
    match_list = soup.find_all(
        'div', attrs={'class': 'matchmain bisai_qukuai'})
    for match in match_list:
        time = match.find('div', attrs={'class': 'whenm'}).text.strip()
        teamname = match.find_all('span', attrs={'class': 'team_name'})
        if teamname[0].string[0:3] == 'php':
            team1_name = "暂无队名"
        else:
            team1_name = teamname[0].string
        # 这里我们采用了css选择器：比原来的属性选择更加方便
        team1_support_level = match.find(
            'span', class_='team_number_green').string

        team2_name = teamname[1].string
        team2_support_level = match.find(
            'span', class_='team_number_red').string

        print('比赛时间：{}，\n 队伍一：{}      胜率 {}\n 队伍二：{}      胜率 {} \n'.format(
            time, team1_name, team1_support_level, team2_name,
            team2_support_level))
def main():
    url= 'http://dota2bocai.com/match'
    print_result(url)

if __name__ == '__main__':
    main()