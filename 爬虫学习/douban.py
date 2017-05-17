import requests
from bs4 import BeautifulSoup

url = 'https://movie.douban.com/people/74224628/collect'
# 构造 Request headers
agent = 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36'
headers = {
	'User-Agent':agent
}
resp = requests.get(url = url)
print(resp.headers)
print(resp.encoding)
soup = BeautifulSoup(resp.text,"lxml")
print('-------')
#print(soup.find('title').string)
items = soup.find_all('div',class_='item')
moives = []
for item in items:
	soup = BeautifulSoup(str(item))
	moive = {}
	moive['title'] = soup.find('em').string
	moive['abstract'] = soup.find('li',class_="intro").string
	moive['date'] = soup.find(class_='date').string
	tags = soup.find(class_='tags')
	if tags:
		moive['tags'] = tags.string
	else:
		moive['tags']=''
	comment = soup.find(class_="comment")
	if comment:
		moive['comment'] = comment.string
	else:
		moive['comment']=''
	moives.append(moive)
print(moives)

