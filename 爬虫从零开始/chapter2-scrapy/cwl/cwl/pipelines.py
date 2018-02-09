# -*- coding: utf-8 -*-

import pymysql
from cwl import utils

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class CwlPipeline(object):

    # 当spider被开启时，这个方法被调用
    def open_spider(self, spider):
        self.db = utils.initDb(spider)

    # 当spider被关闭时，这个方法被调用
    def close_spider(self, spider):
        utils.closeDb(self.db)

    def process_item(self, item, spider):
        print('------------blogPipelineBegin------------')
        nums = item['nums']
        sql = 'INSERT INTO record(qiHao,numOne,numTwo,numThr,numFou,numFiv,numSix,numSec) VALUES("{0}","{1}","{2}","{3}","{4}","{5}","{6}","{7}")'.format(
            item['qiHao'], nums[0], nums[1], nums[2], nums[3], nums[4],
            nums[5], nums[6])
        cursor = self.db.cursor()
        try:
            # 执行sql语句
            print(sql)
            cursor.execute(sql)
            # 执行sql语句
            self.db.commit()
            print('写入数据库成功')
        except:
            # 发生错误时回滚
            print('写入数据库失败')
            self.db.rollback()
        print('------------blogPipelineEnd------------')
