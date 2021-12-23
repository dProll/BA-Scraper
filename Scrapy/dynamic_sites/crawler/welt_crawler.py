from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from dynamic_sites.items import Article



class CrawlerSpider(CrawlSpider):
    name = 'crawler'
    allowed_domains = ['www.welt.de']
    start_urls = ['https://www.welt.de']
    rules = [Rule(LinkExtractor(allow=r'.*'), callback='parse_next',
    follow=True)]

    def parse_next(self, response):
        article = Article()
        url = response.url
        title = response.xpath('//html/head/title/text()').extract_first()
        article['url'] = url
        article['title'] = title.strip()
        comments = response.xpath("//div[@style='font-family: freight, Georgia, serif; font-size: 1.125rem; color: rgb(29, 29, 29); line-height: 1.875rem; overflow-wrap: break-word; white-space: pre-line; padding-right: 3.125rem; margin-left: 45px;']//text()").extract()
        article['comment'] = comments
        #for idc, comment in enumerate(comments):
            #article['comment{}'.format(idc+1)] = comment.strip()
        #if article['comment'] is not None and article['comment'] != [""] and article['title'] is not None:
        if article['title'] is not None and article['title'] != "" and article['comment'] is not None and article['comment'] != []:
            return article 