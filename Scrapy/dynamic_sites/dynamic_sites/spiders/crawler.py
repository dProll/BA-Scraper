from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from dynamic_sites.items import Article
from scrapy import Request


class CrawlerSpider(CrawlSpider):
    name = 'crawler'
    allowed_domains = ['www.merkur.de', 'disqus.com/embed/comments/']
    start_urls = ['https://www.merkur.de/welt/novavax-corona-totimpfstoff-omikron-zulassung-impfstoff-weihnachten-wirkung-covid-lauterbach-zr-91197497.html']
    #rules = [Rule(LinkExtractor(allow=r'.*'), callback='parse',
    #follow=True)]

    def parse(self, response):
        url = response.url
        title = response.xpath('//html/head/title/text()').extract_first()
        iframe_url = response.xpath('//iframe[@title="Disqus"]//@src').get()
        yield { 'title': title, 'url': iframe_url}
            #yield Request(iframe_url, callback=self.next_parse, meta={'url': url, 'title': title})


    # def next_parse(self,response):
    #     article = Article()
    #     article['url'] = response.request.meta['url']
    #     article['title'] = response.request.meta['title']

    #     comments = response.xpath("//div[@class='post-message ']/div/p").getall()
    #     article['comment'] = comments
    #     #for idc, comment in enumerate(comments):
    #         #article['comment{}'.format(idc+1)] = comment.strip()
    #     #if article['comment'] is not None and article['comment'] != [""] and article['title'] is not None and article['title'] != "":
    #     if article['title'] is not None and article['title'] != "":    
    #         return article 