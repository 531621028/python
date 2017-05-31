from selenium import webdriver
from bs4 import BeautifulSoup
try:
  import cPickle as pickle
except ImportError:
  import pickle
import time

print('login')
url = 'http://www.zhihu.com'
driver = webdriver.Chrome('E:\Python\chromedriver.exe')
time.sleep(1)
driver.get(url)
loginTab = driver.find_element_by_css_selector('a[href="#signin"]')
loginTab.click()
login = ''
loginBtns = driver.find_elements_by_css_selector('button.sign-button.submit')
for loginBtn in loginBtns:
	if loginBtn.text == '登录':
		login = loginBtn
print(login.text)
dl = input('确认登录请输入Y：')
if dl == 'Y':
	login.click()
time.sleep(4)
cookies = driver.get_cookies()
with open('E:/Python/爬虫学习/Selenium/cookies.txt','wb') as f:
		pickle.dump(cookies, f)
page = BeautifulSoup(driver.page_source,'lxml')
with open('E:/Python/爬虫学习/Selenium/zhihushouye.html','w',encoding='utf-8') as f:
	f.write(str(page))

driver.quit()

#for cookie in cookies:
#	print("name=%s || value=%s || domain=%s" % (cookie['name'], cookie['value'], cookie['domain']))


#通过id方式定位
#browser.find_element_by_id("kw").send_keys("selenium")

#通过name方式定位
#browser.find_element_by_name("wd").send_keys("selenium")

#通过tag name方式定位
#browser.find_element_by_tag_name("input").send_keys("selenium")

#通过class name 方式定位
#browser.find_element_by_class_name("s_ipt").send_keys("selenium")

#通过CSS方式定位
#browser.find_element_by_css_selector("#kw").send_keys("selenium")

#通过xphan方式定位
#browser.find_element_by_xpath("//input[@id='kw']").send_keys("selenium")