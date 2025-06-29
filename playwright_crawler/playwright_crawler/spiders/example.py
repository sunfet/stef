import scrapy

class ExampleSpider(scrapy.Spider):
    name = 'example'
    start_urls = ['http://example.com']

    def parse(self, response):
        yield {'title': response.xpath('//title/text()').get()}