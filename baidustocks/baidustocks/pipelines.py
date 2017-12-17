# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html



class BaidustocksPipeline(object):
    def process_item(self, item, spider):
        return item

class BaidustocksInfoPipeline(object):
    
    def open_item(self,apider):
        self.f = open('baidustockinfo.txt','w')


    def close_item(self,spider):
        self.f.close()


    def process_item(self, item, spider):
        try:
            with open('baidustockinfo.txt','a+',encoding='utf8') as self.f:
                line = str(dict(item)) + '\n'
                self.f.write(line)
            self.f.close()
        except :
            pass
        return item