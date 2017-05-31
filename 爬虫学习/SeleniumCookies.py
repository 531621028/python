from selenium import webdriver
import time

driver = webdriver.Chrome('E:\Python\chromedriver.exe')
#driver = webdriver.PhantomJS()
driver.get("http://www.zhihu.com")



#向cookie的name 和value添加会话信息。
driver.add_cookie({'name':'Login.Token1','value':'15227','domain':'www.youdao.com'})

#遍历cookies中的name 和value信息打印，当然还有上面添加的信息
for cookie in driver.get_cookies():
    print("%s -> %s" % (cookie['name'], cookie['value']))


# 下面可以通过两种方式删除cookie
# 删除一个特定的cookie
driver.delete_cookie("CookieName")
# 删除所有cookie
driver.delete_all_cookies()

time.sleep(2)
driver.close()