# -*- coding: utf-8 -*-
import scrapy
# import re
# from bs4 import BeautifulSoup
# from scrapy.http import Request
# from coin_spider.items import CoinSpiderItem
class CoinSpider(scrapy.Spider):
    name = 'coin_spider'
    allowed_domains = ['coincheckup.com']
    start_urls = ['https://coincheckup.com/coins/eos/market']

    # def start_request(self):
    # 	for coin_url in ['https://coincheckup.com/coins/eos/investment']:
    # 		url = coin_url
    # 		yield Request(url,self.parse)
    # def parse(self, response):
    #     print(response.text)

    def parse(self,response):
    	# print(response.text)
    	# filename = response.url.split('/')[-2] # eos
    	# with open(filename,'wb') as f:
    	# 	f.write(response.body)
    	for sel in response.xpath('//ul/li'):
    		item = CoinSpiderItem()
    		item['title'] = sel.xpath('a/text()').extract()
    		item['link'] = sel.xpath('a/@href').extract()
    		# item['desc'] = sel.xpath('text()').extract()
    		yield item