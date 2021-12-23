import scrapy
from scrapy import Request

class CrawlerSpider(scrapy.Spider):
    name = 'crawler'
    allowed_domains = ['www.merkur.de', 'disqus.com/embed/comments/']
    start_urls = ['https://www.merkur.de/welt/novavax-corona-totimpfstoff-omikron-zulassung-impfstoff-weihnachten-wirkung-covid-lauterbach-zr-91197497.html']


    def parse(self, response):
        title = response.xpath('//html/head/title/text()').extract_first()
        iframe_url = response.xpath('//iframe[@title="Disqus"]//@src').get()
        yield Request(iframe_url, callback=self.next_parse, meta={'title': title})

    def next_parse(self, response):
        
        title = response.meta.get('title')
        comments = response.xpath("//div[@class='post-message ']/div/p").getall()
        yield {'title': title}
