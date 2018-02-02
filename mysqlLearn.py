import pymysql

# 打开数据库连接
db = pymysql.connect("localhost", "root", "root", "test")
cursor = db.cursor()
cursor.execute("SELECT VERSION()")
data = cursor.fetchone()
print(data)
cursor.close()
print('{},{},{}'.format('zhangk', 'boy', 32))