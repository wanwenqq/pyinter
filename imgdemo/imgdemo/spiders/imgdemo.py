# -*- coding : utf-8 -*-
import scrapy
from imgdemo.items import ImgdemoItem


class imgdemoSpider(scrapy.Spider):
    name = 'imgdemo'
    allowed_domains = ['lab.scrapyd.cn']
    start_urls = ['http://lab.scrapyd.cn/archives/55.html','http://lab.scrapyd.cn/archives/57.html',]
    def parse(self, response):
        item = ImgdemoItem()  # 实例化item
        # 注意imgurls是一个集合也就是多张图片
        item['imgurl'] = response.css(".post img::attr(src)").extract()
        # 抓取文章标题作为图集名称
        item['imgname'] = response.css(".post-title a::text").extract_first()
        yield item

