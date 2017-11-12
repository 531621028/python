# -*- coding: utf-8 -*-
import os
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
dir_path = os.path.dirname(__file__) + '\\'


class ProxyPipeline(object):
    def process_item(self, item, spider):
        open(dir_path + 'kdl_proxy.txt', 'a+').write(item['addr'] + '\n')
        return item
