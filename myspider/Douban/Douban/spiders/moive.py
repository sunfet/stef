import scrapy
from Douban.items import DoubanItem

class MoiveSpider(scrapy.Spider):
    name = "moive"
    allowed_domains = ["douban.com"]
    start_urls = ["https://movie.douban.com/top250"]

    def parse(self, response):
        el_list = response.xpath('//div[@class="info"]')
        for item in el_list:
            yield {
                'name': item.xpath('.//span[@class="title"]/text()').get().split('/')[0],
                'info': item.xpath('.//div[@class="bd"]/p[1]/text()[1]').get().strip(),
                'score': item.xpath('.//span[@class="rating_num"]/text()').get(),
                'desc': item.xpath('.//p[@class="quote"]/span').get()
            }

        next_page = response.xpath('//span[@class="next"]/a/@href').get()
        if next_page:
            yield response.follow(next_page, self.parse)
