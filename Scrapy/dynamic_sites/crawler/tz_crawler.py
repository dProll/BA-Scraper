from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from dynamic_sites.items import Article



class CrawlerSpider(CrawlSpider):
    name = 'crawler'
    allowed_domains = ['www.tz.de']
    start_urls = ['https://www.tz.de']
    rules = [Rule(LinkExtractor(allow=r'.*'), callback='parse_next',
    follow=True)]

    def parse_next(self, response):
        article = Article()
        url = response.url
        title = response.xpath('//html/head/title/text()').extract_first()
        article['url'] = url
        article['title'] = title.strip()
        comments = response.xpath("//div[@class='post-message ']//p").extract()
        article['comment'] = comments
        #for idc, comment in enumerate(comments):
            #article['comment{}'.format(idc+1)] = comment.strip()
        #if article['comment'] is not None and article['comment'] != [""] and article['title'] is not None:
        if article['title'] is not None and article['title'] != "" and article['comment'] is not None and article['comment'] != []:
            return article 