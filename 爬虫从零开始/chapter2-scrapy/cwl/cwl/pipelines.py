# -*- coding: utf-8 -*-

import pymysql
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class CwlPipeline(object):
    def process_item(self, item, spider):
        print('------------blogPipelineBegin------------')
        print('item', item)
        nums = item['nums']
        sql = 'INSERT INTO record(qiHao,numOne,numTwo,numThr,numFou,numFiv,numSix,numSec) VALUES("{0}","{1}","{2}","{3}","{4}","{5}","{6}","{7}")'.format(item['qiHao'], nums[0], nums[1], nums[2], nums[3], nums[4], nums[5], nums[6])
        db = initDb(spider)
        cursor = db.cursor()
        try:
            # 执行sql语句
            print(sql)
            cursor.execute(sql)
            # 执行sql语句
            db.commit()
            print('写入数据库成功')
        except:
            # 发生错误时回滚
            print('写入数据库失败')
            db.rollback()
        print('------------blogPipelineEnd------------')
        closeDb(cursor)


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


def closeDb(cursor):
    cursor.close()
