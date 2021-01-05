# -*- coding: utf-8 -*-
import scrapy
from scrapy_demo.items import ScrapyDemoItem


class EttodaySpider(scrapy.Spider):
    name = 'ettoday'
    allowed_domains = ['www.ettoday.net']
    start_urls = ['https://www.ettoday.net/news/20201004/1824032.htm']

    def parse(self, response):        
        #item = ScrapyDemoItem()
        text = response.xpath('//title/text()').get()
        content = response.xpath('//div[@itemprop="articleBody"]//p/text()').getall()
        print(text)
        print(content)
        
        #yield item