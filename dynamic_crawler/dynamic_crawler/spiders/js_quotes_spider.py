import scrapy
from scrapy_playwright.page import PageMethod
import asyncio

class JsQuotesSpider(scrapy.Spider):
    name = 'js_quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['https://quotes.toscrape.com/js/page/1/']

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(
                url,
                meta=dict(
                    playwright=True,
                    playwright_include_page=True,
                    playwright_page_methods=[
                        PageMethod('wait_for_selector', 'div.quote', timeout=10000),
                    ],
                ),
                callback=self.parse,
                errback=self.errback,
            )

    def parse(self, response):
        quotes = response.xpath('//div[@class="quote"]')
        if not quotes:
            self.logger.warning('No quotes found on page: %s', response.url)

        for quote in quotes:
            yield {
                'text': quote.xpath('.//span[@class="text"]/text()').get(),
                'author': quote.xpath('.//small[@class="author"]/text()').get(),
                'tags': quote.xpath('.//div[@class="tags"]/a/text()').getall(),
            }

        # 翻页逻辑
        next_page = response.xpath('//li[@class="next"]/a/@href').get()
        if next_page:
            yield scrapy.Request(
                response.urljoin(next_page),
                meta=dict(
                    playwright=True,
                    playwright_include_page=True,
                    playwright_page_methods=[
                        PageMethod('wait_for_selector', 'div.quote', timeout=10000),
                    ],
                ),
                callback=self.parse,
                errback=self.errback,
            )

    async def errback(self, failure):
        if 'playwright_page' in failure.request.meta:
            page = failure.request.meta['playwright_page']
            try:
                await page.screenshot(path='error_screenshot.png')
                await page.close()
            except Exception as e:
                self.logger.error('Failed to handle page on error: %s', e)
        self.logger.error(repr(failure))