from selenium import webdriver
from bs4 import BeautifulSoup
try:
  import cPickle as pickle
except ImportError:
  import pickle
import time

url = 'https://www.zhihu.com/question/60214137/answer/175637040'
driver = webdriver.Chrome('E:\Python\chromedriver.exe')
driver.get(url)
cookies = ''
with open('E:/Python/爬虫学习/Selenium/cookies.txt','rb') as f:
	cookies = pickle.load(f)
driver.delete_all_cookies()
for cookie in cookies:
	driver.add_cookie(cookie)
driver.get('https://www.zhihu.com/question/60214137/answer/175637040')
#获取查看更多的按钮
#viewmore = driver.find_elements_by_css_selector('button.Button.QuestionMainAction')
#获取查看所有按钮
viewall = driver.find_elements_by_css_selector('a.QuestionMainAction')
print(len(viewall))
viewall[0].click()
time.sleep(1)
page = BeautifulSoup(driver.page_source,'lxml')
with open('E:/Python/爬虫学习/Selenium/60214137.html','w',encoding='utf-8') as f:
	f.write(str(page))
#获取每一个回答的内容列表
anwsers = page.select('div.List-item')
print(len(anwsers))
for anwser in anwsers:
	anwserInfo = {}
	imglist=[]
	anwserInfo['name'] = anwser.select('div.UserLink.AuthorInfo-name').select('div.UserLink-link').string
	print(anwserInfo)