import pymysql


def initDb(spider):
    settings = spider.settings
    host = settings['HOST']
    port = settings['PORT']
    username = settings['USERNAME']
    password = settings['PASSWORD']
    dbname = settings['DBNAME']
    print(host, port, username, password, dbname)
    db = pymysql.connect(host=host, user=username, password=password, database=dbname, port=port, charset='utf8')
    return db


def closeDb(db):
    db.close()