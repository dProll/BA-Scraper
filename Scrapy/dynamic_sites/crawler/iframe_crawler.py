from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from dynamic_sites.items import Article
from scrapy import Request


class CrawlerSpider(CrawlSpider):
    name = 'crawler'
    allowed_domains = ['www.tz.de', 'disqus.com']
    start_urls = ['https://www.tz.de']
    rules = [Rule(LinkExtractor(allow=r'.*'), callback='parse_next',
    follow=True)]

    def parse_next(self, response):
        
        #Rule(LinkExtractor(allow="//article[@class='product_pod']/div/a"), callback='parse_item', follow=True)
        url = response.url
        title = response.xpath('//html/head/title/text()').extract_first()
        #try:
        iframe_url = response.xpath('//iframe[@title="Disqus"]/@src').get()
        yield Request(iframe_url, callback=self.parse_next_next, meta={'url': url, 'title': title})
        #except:


    def parse_next_next(self,response):
        article = Article()
        article['url'] = response.request.meta['url']
        article['title'] = response.request.meta['title']

        comments = response.xpath("//div[@class='post-message ']/div/p").getall()
        article['comment'] = comments
        #for idc, comment in enumerate(comments):
            #article['comment{}'.format(idc+1)] = comment.strip()
        #if article['comment'] is not None and article['comment'] != [""] and article['title'] is not None:
        if article['title'] is not None and article['title'] != "":    
            return article 