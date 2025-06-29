import scrapy
from wangyi.items import WangyiItem


class JobSpider(scrapy.Spider):
    name = "job"
    #2. 检查域名
    allowed_domains = ["hr163.com"]
    #1. 修改start_urlurl
    start_urls = ["https://hr.163.com/api/hr163/position/query.do?curPage=1&pageSize=10"]

    def parse(self, response):
        #提取数据
        #获取所有职位节点列表
        data = response.json()
        
        #遍历节点列表
        for node in data['result']['list']:
            #设置过滤条件
          
            
            
            item = WangyiItem()
            item['职位'] = node.get("name")
            item['实习全职'] = node.get("recruitType")
            item['地址'] = node.get("workPlace")
            item['公司'] = node.get("companyName")
            item['岗位'] = node.get("category")
            item['人数'] = node.get("recruitNum")
            item['学历'] = node.get("eduLevel")
            item['经验'] = node.get("workExp")
            yield item
            '''
            item['link'] = response.urljoin(node.xpath('./span/@href')[0].extract())
            # item['link'] = 'https:hr.163.com' + node.xpath('./span/@href()')[0].extract()
            yield scrapy.Request(
                url = item['link'],
                callback = parse_detail,
                meta = {'item':item}
            )
            '''




            
        #模拟翻页
        cur_page = data['result']['curPage']
        total_page = data['result']['totalPageCount']
        if cur_page < total_page:
            next_page = cur_page + 1
            next_url = f"https://hr.163.com/api/hr163/position/query.do?curPage={next_page}&pageSize=10"
            yield scrapy.Request(next_url, callback=self.parse) #与第一页处理方法相同,所以用callback = self.parse

        #能找到@href的情况
        # part_url = response.xpath('//*[@id="m-job-list"]/div[2]/div[2]/div/div/div[2]/div/div/div[2]/div/div[1]/div/a/@href').extract_first()
        # if part_url != 'ant-pagination-item-link':
        #     next_url = response.urljoin(part_url)
        #     yield scrapy.Request(next_url, callback=self.parse) 

    def parse_detail(self, response):
        #meta传参
        item = response.meta['item']
        #提取剩余字段信息
        item['岗位职责'] = response.xpath('').extract()
        item['岗位要求'] = response.xpath('').extract()
        #返回引擎
        yield item
       







