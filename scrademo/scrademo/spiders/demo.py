# -*- coding: utf-8 -*-
import scrapy

class demo(scrapy.Spider):
    name = 'demo'

    # start_urls = [  #另外一种写法，无需定义start_requests方法
    #     'http://lab.scrapyd.cn/page/1/',
    # ]



    def start_requests(self):
        url = 'http://lab.scrapyd.cn/'
        tag = getattr(self, 'tag', None)  # 获取tag值，也就是爬取时传过来的参数
        if tag is not None:  # 判断是否存在tag，若存在，重新构造url
            url = url + 'tag/' + tag  # 构造url若tag=爱情，url= 
        yield scrapy.Request(url=url, callback=self.parse) #爬取到的页面如何处理？提交给parse方法处理


    # start_urls = ['http://lab.scrapyd.cn']


    def parse(self, response):
        # page = response.url.split("/")[-2]     #根据上面的链接提取分页,如：/page/1/，提取到的就是：1
        # filename = 'mingyan-%s.html' % page    #拼接文件名，如果是第一页，最终文件名便是：mingyan-1.html
        # with open(filename, 'wb') as f:        #python文件操作，不多说了；
        #     f.write(response.body)             #刚才下载的页面去哪里了？response.body就代表了刚才下载的页面！
        # self.log('保存文件: %s' % filename)      # 打个日志

        mingyan = response.css('div.quote')
       

        for v in mingyan:  # 循环获取每一条名言里面的：名言内容、作者、标签

            text = mingyan.css('.text::text').extract_first()  # 提取名言
            # autor = mingyan.css('.author::text').extract_first()  # 提取作者
            tags = mingyan.css('.tags .tag::text').extract()  # 提取标签
            tags = ','.join(tags)  # 数组转换为字符串

            fileName = '%s-语录.txt' % tags  # 爬取的内容存入文件，文件名为：作者-语录.txt
            with open(fileName, "a+") as f: # 追加写入文件
                f.write(text)  # 写入名言内容
                f.write('\n')  # 换行
                f.write('标签：'+tags)  # 写入标签
                f.write('\n-------\n')
                f.close()  # 关闭文件操作

        next_page = response.css('li.next a::attr(href)').extract_first() 
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)

