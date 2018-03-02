# -*- coding: utf-8 -*-
import scrapy


class TiebaSpider(scrapy.Spider):
    name = 'Tieba'
    allowed_domains = ['tieba.baidu.com']
    start_urls = ['http://tieba.baidu.com/']

    def parse(self, response):
        pass
