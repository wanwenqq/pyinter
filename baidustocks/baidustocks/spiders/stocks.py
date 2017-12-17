# -*- coding: utf-8 -*-
import scrapy
import re

class StocksSpider(scrapy.Spider):
    name = "stocks"
    # allowed_domains = ["baidu.com"]
    start_urls = ['http://quote.eastmoney.com/stocklist.html']

    def parse(self, response):
        i = 0
        for href in response.css('a::attr(href)').extract():
            i += 1
            if i<100:
                continue
            if i>200:
                return
            try:
                stocks = re.findall(r'[s][hz]\d{6}',href)[0]
                url = 'https://gupiao.baidu.com/stock/' + stocks + '.html'
                yield scrapy.Request(url,callback=self.parser_stocks)
            except :
                continue

    def parser_stocks(self,response):
        infoDic = {}
        stockInfo = response.css('.stock-bets')
        name = stockInfo.css('.bets-name').extract()[0]
        keylist = stockInfo.css('dt').extract()
        vallist = stockInfo.css('dd').extract()
        for i in range(len(keylist)):
            key = re.findall(r'>.*</dt>',keylist[i])[0][1:-5]
            try:
                val = re.findall(r'\d+\.?.*</dd>',vallist[i])[0][0:-5]
            except :
                val = '--'
            infoDic[key] = val
        infoDic.update({'股票名称':re.findall('\s.*\(',name)[0].split()[0] + re.findall('\>.*\<',name)[0][1:-1]})
        yield infoDic