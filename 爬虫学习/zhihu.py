import requests
from bs4 import BeautifulSoup
import os,time
import re
import shutil

# 构造 Request headers
headers = {
	'Connection': 'Keep-Alive',
    'Accept': 'text/html, application/xhtml+xml, */*',
    'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Accept-Encoding': 'gzip, deflate',
    'Host': 'www.zhihu.com',
    'DNT': '1'
}
session = requests.Session()
url = 'https://www.zhihu.com/question/47990673'
cookie = {	'd_c0':'AGACnA8gUAuPTrxdeHgEhKevxOV4VPxRKN4=|1487135674',
			'q_c1':'0c1539ee1af24203bc9835ff1779f075|1494205348000|1487135674000',
			'capsion_ticket':'2|1:0|10:1494205495|14:capsion_ticket|44:YzFkNjVkNmRmNTM0NDkxMDlkM2UwODkzZTU3NmRlOTA=|15d43243a47974acd7ddaed2a7cb28b20c4eb3eaf0fc074d6cf5ddaaff72daa5',
			'_zap':'9781f02b-03d6-4201-95f8-7fe6725afc46',
			'__utma':'51854390.1323194982.1487135673.1487206449.1495004381.4',
			'__utmz':'51854390.1495004381.4.4.utmcsr=baidu|utmccn=(organic)|utmcmd=organic',
			'__utmv':'51854390.000--|3=entry_date=20170215=1',
			'r_cap_id':'ZjQ4MjNjNGUwZTY5NDQ5OWI5YjU0YmMyNmRmNzg3ZjE=|1495005061|7902450a86791427195b433e07015a3c62dfe654',
			'cap_id':'MTUxYjBiM2YxNzM0NGY5YzlkNWRiNDg5ZTg3NWIxMDI=|1495005061|4bbeafade2393cb6c93ab4b9918b4e6dfca21e8d',
			'aliyungf_tc':'AQAAAMcRhA5CNwYAB8JF06CrT+qhD/RC',
			'acw_tc':'AQAAAEJDZhO9AAcAB8JF0way1YkHZ7Vp',
			'z_c0':'Mi4wQUFCQVVaY21BQUFBWUFLY0R5QlFDeGNBQUFCaEFsVk5IWVZEV1FDUHhFNC1Ra2htdUNTc1ZycjRWQUU5NXdVcjdB|1495021750|8039053d8af01e4426b2b0c29e325a2c35122615'
		}
session.cookies.update(cookie)
response = session.get(url=url,headers=headers)
def ungzip(data):
    try:
        print("正在解压缩...")
        data = gzip.decompress(data)
        print("解压完毕...")
    except:
        print("未经压缩，无需解压...")
    return data
#保存图片
def saveImage(url, path):
    resp = requests.get(url)
    if resp.status_code == 200:
        with open(path, 'wb') as f:
        	f.write(resp.content)

data = ungzip(response.text)
soup = BeautifulSoup(data,'lxml')
with open('zhihu.html','wb') as f:
	f.write(response.content)
anwsers = soup.find_all(class_='List-item')
re_imageurl = re.compile(r'^(http)')
print(len(anwsers))
for anwser in anwsers:
	imgsoup = BeautifulSoup(str(anwser))
	imgs = imgsoup.find_all('img')
	imglist=[]
	if imgs:
		for img in imgs:
			print(dict(img.attrs))
			imgurl = dict(img.attrs)['src']
			if re_imageurl.match(imgurl):
				imglist.append(imgurl)
print(imglist)
if 'https://pic1.zhimg.com/v2-4ad12f3556cad910e34b58812747a244_b.jpg' in imglist:
	print('存在')
saveImage('https://pic1.zhimg.com/v2-4ad12f3556cad910e34b58812747a244_b.jpg','e://1.jpg')