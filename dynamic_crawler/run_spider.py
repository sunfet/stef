import os
import sys
from scrapy.crawler import CrawlerProcess
from dynamic_crawler.spiders.js_quotes_spider import JsQuotesSpider

def run_spider():
    # 设置项目路径
    sys.path.append(os.path.abspath("."))

    # 创建爬虫进程
    process = CrawlerProcess({
        'BOT_NAME': 'dynamic_crawler',
        'SPIDER_MODULES': ['dynamic_crawler.spiders'],
        'ITEM_PIPELINES': {},
        'NEWSPIDER_MODULE': 'dynamic_crawler.spiders',
        'USER_AGENT': 'Mozilla/5.0',
        'ROBOTSTXT_OBEY': False,
        'LOG_LEVEL': 'DEBUG',
        'FEEDS': {
            'quotes.json': {
                'format': 'json',
                'overwrite': True,
            },
        },
        # Playwright 配置 - 增加浏览器启动参数
        'DOWNLOAD_HANDLERS': {
            "http": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
            "https": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
        },
        'PLAYWRIGHT_DEFAULT_NAVIGATION_TIMEOUT': 10000,  # 增加页面加载超时时间
        'PLAYWRIGHT_BROWSER_TYPE': 'chromium',  # 使用 chromium 浏览器
        'PLAYWRIGHT_LAUNCH_OPTIONS': dict(
            headless=True,  # 使用无头模式
            args=["--disable-gpu", "--no-sandbox"]  # 禁用 GPU 加速和沙箱
        ),
        'TWISTED_REACTOR': 'twisted.internet.asyncioreactor.AsyncioSelectorReactor',
    })

    # 启动爬虫
    process.crawl(JsQuotesSpider)
    process.start()

if __name__ == '__main__':
    run_spider()