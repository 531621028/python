from datetime import datetime
now = datetime.now()
print(now)
dt = datetime(2015, 4, 19, 12, 20)
print(dt)
print(dt.timestamp())
t = dt.timestamp()
print(datetime.fromtimestamp(t))
cday = datetime.strptime('2015-6-1 18:19:54','%Y-%m-%d %H:%M:%S')
print(cday)
print(now.strftime('%a,%b,%d %H:%M:%M'))
#对日期和时间进行加减实际上就是把datetime往后或往前计算，得到新的datetime。加减可以直接用+和-运算符，不过需要导入timedelta这个类
from datetime import timedelta
print(now+timedelta(hours=10))
print(now+timedelta(days=2,hours=10))
import re
from datetime import timezone
print(re.split(r'[UTC\:]','UTC+5:00'))
def to_timestamp(dt_str, tz_str):
	dt = datetime.strptime(dt_str,'%Y-%m-%d %H:%M:%S')
	print(dt)
	dt_tz = timezone(timedelta(hours=int(re.split(r'[UTC\:]',tz_str)[3])))
	dt = dt.replace(tzinfo=dt_tz)
	print(dt)
	return dt.timestamp()
t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
assert t1 == 1433121030.0
