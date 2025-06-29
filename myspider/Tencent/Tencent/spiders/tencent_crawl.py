import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class TencentCrawlSpider(CrawlSpider):
    name = "tencent_crawl"
    allowed_domains = ["tencent.com"]
    start_urls = ["https://tencent.com"]
    #使用rule类生产链接提取规则对象
    #LinkExtractor用于设置链接提取规则,一般使用allow,接受正则表达式
    #follow 决定是否在链接提取器提取的链接对应的响应中继续应用链接提取器提取链接

    #提取详情页
    # rules = (Rule(LinkExtractor(allow=r"Items/"), callback="parse_item", )
    #翻页
    rules = (Rule(LinkExtractor(allow=r"Items/"), callback="parse_item", follow=True),)

    def parse_item(self, response):
        item = {}
        #item["domain_id"] = response.xpath('//input[@id="sid"]/@value').get()
        #item["name"] = response.xpath('//div[@id="name"]').get()
        #item["description"] = response.xpath('//div[@id="description"]').get()
        yield item
