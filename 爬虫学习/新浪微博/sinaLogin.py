from selenium import webdriver
from bs4 import BeautifulSoup
try:
  import cPickle as pickle
except ImportError:
  import pickle
import time

url = 'http://weibo.com'
def getLoginCookie(name,pwd):
	driver = webdriver.Chrome('E:\Python\chromedriver.exe')
	time.sleep(1)
	driver.get(url)


if __name__ == '__main__':
	getLoginCookie('','')