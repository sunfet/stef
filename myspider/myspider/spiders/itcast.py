import scrapy
from myspider.items import MyspiderItem

class ItcastSpider(scrapy.Spider):
    name = "itcast"
    #2 检查域名是否一致
    allowed_domains = ["itheima.com"]
    #1 修改起始URL
    start_urls = ["https://www.itheima.com/teacher.html#ajavaee?cz-pc-dh"]

    #3 完善爬取逻辑
    def parse(self, response):
        #定义对于网站的相关操作
        #获取教师节点
        node_list = response.xpath('//div[@class="main_mask"]/h2')
        # node_list = response.xpath('//*[@id="mCSB_1_container"]/ul/li/div[2]/div/h2')
        
        print(len(node_list)) #输出教师节点的个数
        #遍历教师节点列表
        for node in node_list:
            # item = {}
            item = MyspiderItem()
            #xpath返回的是选择器对象列表
            item['name'] = node.xpath('./h2/text()')[0].extract()
            item['title'] = node.xpath('.h2/span/text()')[0].extract()
            item['desc'] = node.xpath('.p/text()')[0].extract()
            
            yield item