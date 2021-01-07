import scrapy
from homework.items import HomeworkItem

class WomanySpider(scrapy.Spider):
    name = 'womany'
    allowed_domains = ['womany.net']
    start_urls = ['http://womany.net/']

    def parse(self, response):
        item = HomeworkItem()
        item['title'] = response.xpath('//title/text()').get()
        item['content'] = response.xpath('//meta/@content').getall()
        yield item