import scrapy


class WomanySpider(scrapy.Spider):
    name = 'womany'
    allowed_domains = ['womany.net']
    start_urls = ['http://womany.net/']

    def parse(self, response):
        title = response.xpath("//title.text()").get()
        print(title)
