import requests
url = 'http://weibo.com/'
r = requests.get(url=url)
print(r.status_code)
url = 'http://dict.baidu.com/s'
postdata = {
	'wd':'python'
}
r = requests.get(url=url, params=postdata)  #带参数的GET请求
print(r.url)
#print(r.text)
#reauest高级用法
s = requests.Session()

s.get('http://httpbin.org/cookies/set/sessioncookie/123456789')
r = s.get("http://httpbin.org/cookies")

print(r.text)
