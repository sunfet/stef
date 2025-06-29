# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json


class MyspiderPipeline:
    def __init__(self):
        self.file = open('data.json','wb')

    #将item对象强转成字典
    item = dict(item)
    #默认使用完管道之后需要将数据返回给引擎
    def process_item(self, item, spider):
        #将字典数据序列化
        json_data = json.dumps(item)
        #将数据写入文件
        self.file.write(json_data)
        return item
    
    def __del__(self):
        self.file.close()
