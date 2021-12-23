from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from static_sites.items import Article


class CrawlerSpider(CrawlSpider):
    name = 'crawler'
    allowed_domains = ['www.focus.de']
    start_urls = ['https://www.focus.de']
    rules = [Rule(LinkExtractor(allow=r'.*'), callback='parse_items',
    follow=True)]
    
    def parse_items(self, response):
        article = Article()
        url = response.url
        title = response.xpath('/html/head/title/text()').extract_first()
        comments = response.xpath('//p[@class="text"]/text()').extract()

        article['url'] = url
        article['title'] = title
        for idc, comment in enumerate(comments):
            article['comment{}'.format(idc+1)] = comment.strip()
        if article['comment1'] is not None and article['comment1'] != [""] and article['title'] is not None:
            return article 