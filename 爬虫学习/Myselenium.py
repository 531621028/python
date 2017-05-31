from selenium import webdriver 
from bs4 import BeautifulSoup
import time
url = 'http://baike.baidu.com/starrank?fr=lemmaxianhua' 
driver = webdriver.PhantomJS()  
driver.get(url)
print(driver.get_cookies())

name_counter = 1
page = 0;
while page < 2: # 共50页，这里是手工指定的
	soup = BeautifulSoup(driver.page_source, "lxml")
	current_names = soup.select('div.ranking-table') # 选择器用ranking-table css class，可以取出包含本周、上周的两个table的div标签
	for current_name_list in current_names:
		# print current_name_list['data-cat']
		if current_name_list['data-cat'] == 'thisWeek': # 这次我只想抓取本周，如果想抓上周，改一下这里为lastWeek即可
			names = current_name_list.select('td.star-name > a') # beautifulsoup选择器语法
			counter = 0;
			for star_name in names:
				counter = counter + 1;
				print(star_name.text) # 明星的名字是a标签里面的文本，虽然a标签下面除了文本还有一个与文本同级别的img标签，但是.text输出的只是文本而已
				name_counter = name_counter + 1;
	next_step = driver.find_element_by_xpath("//a[contains(text(),'下一页')]")
	#next_step = driver.find_element_by_xpath('//a[@class="pTag next"]')
	print(next_step)
	if next_step:
		next_step.click() # selenium的xpath用法，找到包含“下一页”的a标签去点击
	page = page + 1
	time.sleep(2) # 睡2秒让网页加载完再去读它的html代码

print(name_counter) # 共爬取得明星的名字数量
driver.quit()