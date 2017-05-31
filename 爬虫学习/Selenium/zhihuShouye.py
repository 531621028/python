from selenium import webdriver
from bs4 import BeautifulSoup
try:
  import cPickle as pickle
except ImportError:
  import pickle
import time

url = 'http://www.zhihu.com'
driver = webdriver.Chrome('E:\Python\chromedriver.exe')
time.sleep(1)
driver.get(url)
cookies = ''
with open('E:/Python/爬虫学习/Selenium/cookies.txt','rb') as f:
	cookies = pickle.load(f)
driver.delete_all_cookies()
for cookie in cookies:
	driver.add_cookie(cookie)
time.sleep(2)
driver.get('https://www.zhihu.com')
for cookie in cookies:
	print("name=%s || value=%s || domain=%s" % (cookie['name'], cookie['value'], cookie['domain']))
page = BeautifulSoup(driver.page_source,'lxml')
with open('E:/Python/爬虫学习/Selenium/zhihushouye.html','w',encoding='utf-8') as f:
	f.write(str(page))