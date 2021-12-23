# Scrapy settings for the dynamic_sites project

# Name of the Crawler
BOT_NAME = 'dynamic_sites'

# Spider Modules
SPIDER_MODULES = ['dynamic_sites.spiders']
NEWSPIDER_MODULE = 'dynamic_sites.spiders'

# Crawl responsibly by identifying the crawler on the user-agent
USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Access to the Selenium Request-Response middleware
DOWNLOADER_MIDDLEWARES = {
    'dynamic_sites.middlewares.SeleniumMiddleware': 543,
}

# Outputs the data in clean utf-8 format
FEED_EXPORT_ENCODING = 'utf-8'