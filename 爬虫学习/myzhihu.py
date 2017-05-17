import requests
from bs4 import BeautifulSoup
import os,time
import re

# 构造 Request headers
agent = 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36'
headers = {
	'Host':'www.zhihu.com',
	'Referer':'https://www.zhihu.com/',
	'User-Agent':agent
}
# 构造用于网络请求的session
session = requests.Session()
homeurl = 'https://www.zhihu.com'
homeresponse = session.get(url=homeurl,headers=headers)
homesoup = BeautifulSoup(homeresponse.text,'html.parser')
xsrfinput = homesoup.find('input',{'name':'_xsrf'})
xsrf_token = xsrfinput['value']
print("获取到的xsrf_token为： ", xsrf_token)

#获取验证码文件
randomtime = str(int(time.time()*1000))
captchaurl = 'https://www.zhihu.com/captchaurl.gif?r='+randomtime+'&type=login'
capthcharesponse = session.get(url = captchaurl,headers=headers)
with open('checkcode.jpg','wb') as f:
	f.write(capthcharesponse.content)

captcha = input('请输入验证码')
print(captcha)
#开始登陆
headers['X-Xsrftoken'] = xsrf_token
headers['X-Requested-With'] = 'XMLHttpRequest'
loginurl = 'https://www.zhihu.com/login/email'
postdata = {
	'_xsrf': xsrf_token,
    'email': '531621028@qq.com',
    'password': '531621028hu'
}
loginresponse = session.post(url = loginurl,headers = headers,data = postdata)
print('服务器端返回响应码：', loginresponse.status_code)
print(loginresponse.json())



