import scrapy


class YahooSpider(scrapy.Spider):
    name = 'yahoo'
    allowed_domains = ['tw.yahoo.com']
    start_urls = ['http://tw.yahoo.com/']

    def parse(self, response):
        item = HomeworkItem()
        item['title'] = response.xpath('//title/text()').get()
        item['content'] = response.xpath('//meta/@content').getall()
        yield item
        
        
        
        
        
