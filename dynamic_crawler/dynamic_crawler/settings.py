# Scrapy 设置文件

BOT_NAME = 'dynamic_crawler'

SPIDER_MODULES = ['dynamic_crawler.spiders']
NEWSPIDER_MODULE = 'dynamic_crawler.spiders'

# Playwright 设置
DOWNLOAD_HANDLERS = {
    "http": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
    "https": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
}

TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"

# 日志级别
LOG_LEVEL = 'DEBUG'

# 禁用 robots.txt 规则（测试环境可用）
ROBOTSTXT_OBEY = False

# 下载延迟
DOWNLOAD_DELAY = 1.0

# 并发请求限制
CONCURRENT_REQUESTS = 4

# 启用 Cookies
COOKIES_ENABLED = True

# 默认请求头
DEFAULT_REQUEST_HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
}

# 启用中间件
SPIDER_MIDDLEWARES = {
}

DOWNLOADER_MIDDLEWARES = {
}

# 启用扩展
EXTENSIONS = {
}

# ITEM_PIPELINES
ITEM_PIPELINES = {
}