# -*- coding: utf-8 -*-

import os
import pymysql
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class BlogPipeline(object):
    def process_item(self, item, spider):
        print('------------blogPipelineBegin------------')
        db = initDb(spider)
        cursor = db.cursor()
        sql = 'INSERT INTO blog(title,slug,content,createTime,author) VALUES("{0}","{1}","{2}","{3}","{4}")'.format(item['article_name'],item['article_slug'],item['article_content'],item['article_ctime'],item['article_author'])
        try:
            # 执行sql语句
            cursor.execute(sql)
            # 执行sql语句
            db.commit()
        except:
            # 发生错误时回滚
            db.rollback()
        print('------------blogPipelineEnd------------')


def initDb(spider):
    settings = spider.settings
    host = settings['HOST']
    port = settings['PORT']
    username = settings['USERNAME']
    password = settings['PASSWORD']
    dbname = settings['DBNAME']
    db = pymysql.connect(host=host, user=username, password=password, database=dbname, port=port, charset='utf8')
    return db

def closeDb(cursor):
    cursor.close()
