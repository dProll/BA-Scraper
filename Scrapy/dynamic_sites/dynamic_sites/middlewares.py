# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from selenium import webdriver
from scrapy.http import HtmlResponse
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys 
# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchFrameException, NoSuchElementException




class DynamicSitesSpiderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, or item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request or item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class DynamicSitesDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


# Middleware to extend the request made for every link. 
# Opens a dynamic browser window in the back and scrolls down to the bottom of every site. 
# 1 second stop to make sure every datapoint gets collected and returns the Selenium-Object as a HTMLResponse Object.
class SeleniumMiddleware(object):

    def __init__(self):
        #chrome_options = Options()
        #chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome()#options=chrome_options)

    # Here you get the request you are making to the urls with the LinkExtractor found and use selenium to get them and return a response.
    def process_request(self, request, spider):
        self.driver.get(request.url)
        element = self.driver.find_element_by_xpath('//div[@id="disqus_thread"]')
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(1)
        body = self.driver.page_source
        return HtmlResponse(self.driver.current_url, body=body, encoding='utf-8', request=request)




        # try:
        #     self.driver.switch_to.frame(1)
        # except NoSuchFrameException:
        #     pass
        # except NoSuchElementException:
        #     pass
        #time.sleep(1)
        # try:
        #     WebDriverWait(self.driver, 3).until(expected_conditions.presence_of_element_located((By.XPATH, '//div[@class="post-message "]/div/p/text()')))
        # except:
        #     pass
        #self.driver.execute_script("window.scrollTo(0, 5000);")
        #self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        #time.sleep(5)
        #self.driver.sendKeys(Keys.END)
        #self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        #self.driver.find_element_by_xpath('//div[@class="post-message "]//p'):
        # self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        # self.driver.execute_script('window.scrollTo(0, document.getElementByXpath("page-manager").scrollHeight);')
        # self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        # self.driver.execute_script("window.scrollTo(0, -500);")