import requests
from bs4 import BeautifulSoup
import os,time
import re

# 构造 Request headers
headers = {
	'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
	'Accept-Encoding':'gzip, deflate, sdch, br'
	'Accept-Language':'zh-CN,zh;q=0.8'
	'Cache-Control':'max-age=0'
	'Connection':'keep-alive'
	'Cookie':'d_c0="AGACnA8gUAuPTrxdeHgEhKevxOV4VPxRKN4=|1487135674"; q_c1=0c1539ee1af24203bc9835ff1779f075|1494205348000|1487135674000; capsion_ticket="2|1:0|10:1494205495|14:capsion_ticket|44:YzFkNjVkNmRmNTM0NDkxMDlkM2UwODkzZTU3NmRlOTA=|15d43243a47974acd7ddaed2a7cb28b20c4eb3eaf0fc074d6cf5ddaaff72daa5"; _zap=9781f02b-03d6-4201-95f8-7fe6725afc46; __utma=51854390.1323194982.1487135673.1487206449.1495004381.4; __utmz=51854390.1495004381.4.4.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmv=51854390.000--|3=entry_date=20170215=1; r_cap_id="ZjQ4MjNjNGUwZTY5NDQ5OWI5YjU0YmMyNmRmNzg3ZjE=|1495005061|7902450a86791427195b433e07015a3c62dfe654"; cap_id="MTUxYjBiM2YxNzM0NGY5YzlkNWRiNDg5ZTg3NWIxMDI=|1495005061|4bbeafade2393cb6c93ab4b9918b4e6dfca21e8d"; aliyungf_tc=AQAAAMcRhA5CNwYAB8JF06CrT+qhD/RC; acw_tc=AQAAAEJDZhO9AAcAB8JF0way1YkHZ7Vp; z_c0=Mi4wQUFCQVVaY21BQUFBWUFLY0R5QlFDeGNBQUFCaEFsVk5IWVZEV1FDUHhFNC1Ra2htdUNTc1ZycjRWQUU5NXdVcjdB|1495020948|357ef12d127c0f83ff79c0be93d2e98f00a69191'
	'Host':'www.zhihu.com'
	'Referer':'https://www.baidu.com/link?url=ky27NumghdUr0obLi9BwK1x-AO2-DDAzeGlY1kZWD5W&wd=&eqid=b109ad590005e85d00000003591c3590'
	'Upgrade-Insecure-Requests':1
	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
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



