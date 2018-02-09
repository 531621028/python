# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from jd import utils


class JdPipeline(object):
    # 当spider被开启时，这个方法被调用
    def open_spider(self, spider):
        self.db = utils.initDb(spider)

    # 当spider被关闭时，这个方法被调用
    def close_spider(self, spider):
        utils.closeDb(self.db)

    def process_item(self, item, spider):
        print('------------blogPipelineBegin------------')
        print('item', item)
        sql = 'INSERT INTO jd_good(good_num,good_title,good_name,price,comment_sum,shop_name,link,date) VALUES("{0}","{1}","{2}","{3}","{4}","{5}","{6}","{7}")'.format(
            item['good_num'], item['good_title'], item['good_name'],
            item['price'], item['comment_sum'], item['shop_name'],
            item['link'], item['date'])
        cursor = self.db.cursor()
        try:
            # 执行sql语句
            print(sql)
            cursor.execute(sql)
            # 执行sql语句
            self.db.commit()
            print('写入数据库成功')
        except Exception as e:
            # 发生错误时回滚
            print('写入数据库失败', e)
            self.db.rollback()
        print('------------blogPipelineEnd------------')
