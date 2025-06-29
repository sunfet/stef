# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json
from pymongo import MongoClient

class WangyiPipeline:
    """处理job爬虫的数据管道，将数据写入JSON文件"""
    
    def open_spider(self, spider):
        """在爬虫开启时创建输出文件"""
        if hasattr(spider, 'name') and spider.name == 'job':
            self.file = open('wangyi.json', 'w')
    def process_item(self, item, spider):
        if spider.name == 'job':
            item = dict(item)

            str_data = json.dumps(item, ensure_ascii=False) + ',\n'
            self.file.write(str_data)
        return item
    
    def close_spider(self, spider):
        if spider.name == 'job':
            self.file.close()

class Wangyijob2Pipeline:
    """处理job2爬虫的数据管道，将数据写入JSON文件"""
    
    def open_spider(self, spider):
        """在爬虫开启时创建输出文件"""
        if hasattr(spider, 'name') and spider.name == 'job':
            self.file = open('wangyi.json', 'w')
    def process_item(self, item, spider):
        if spider.name == 'job2':
            item = dict(item)

            str_data = json.dumps(item, ensure_ascii=False) + ',\n'

            self.file.write(str_data)
        return item
    
    def close_spider(self, spider):
        if spider.name == 'job2':
            self.file.close()
class MongoPipeline(object):
    # 没有做spider判断,都要运行
    def open_spider(self, spider):
        self.client = MongoClient('127.0.0.1', 27017)
        self.db = self.client['itcast']
        self.collection = self.db['wangyi']

    def process_item(self, item, spider):
        data = dict(item)
        self.collection.insert(data)
        return item

    def close_spider(self, spider):
        self.client.close()