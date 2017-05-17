s = r'ABC\\-001'
import re
#match()方法判断是否匹配，如果匹配成功，返回一个Match对象
#\s可以匹配一个空格（也包括Tab等空白符），所以\s+表示至少有一个空格，例如匹配' '，' '等
#^表示行的开头，^\d表示必须以数字开头。
#$表示行的结束，\d$表示必须以数字结束。
print(re.match(r'^\d{3}\-\d{3,8}$','010-12345'))
print(re.match(r'^\d{3}\-\d{3,8}$', '010-12345'))
print(re.split(r'\s+', 'a b   c'))
#除了简单地判断是否匹配之外，正则表达式还有提取子串的强大功能。用()表示的就是要提取的分组（Group）
m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
#group(0)永远是原始字符串，group(1)、group(2)……表示第1、2、……个子串
print(m.group(0))
print(m.group(1))
print(m.group(2))
print(m.groups())
#正则匹配默认是贪婪匹配，也就是匹配尽可能多的字符
print(re.match(r'^(\d+)(0*)$', '102300').groups())
#\d+采用贪婪匹配，直接把后面的0全部匹配了，结果0*只能匹配空字符串了。
#必须让\d+采用非贪婪匹配（也就是尽可能少匹配），才能把后面的0匹配出来，加个?就可以让\d+采用非贪婪匹配
print(re.match(r'^(\d+?)(0*)$', '102300').groups())
#编译正则表达式
re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
#使用正则表达式进行匹配
print(re_telephone.match('010-12345').groups())
email = re.compile(r'(\S+?)@(\S+?).com$')
print(email.match('someone@gmail.com').groups())
print(email.match('bill.gates@microsoft.com').groups())
email = re.compile(r'\<(\S+?)\s(\S+?)\>\s(\S+?)@(\S+?).org$')
print(email.match('<Tom Paris> tom@voyager.org').groups())
url = re.compile(r'^(https://)([A-Za-z0-9.]+)/([A-Za-z0-9_]+).([a-z]+)$')
print(url.match('https://pic1.zhimg.com/7754c831451993841cd23eaa26613754_xs.jpg').groups())

