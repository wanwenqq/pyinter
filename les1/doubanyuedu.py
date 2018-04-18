# -*- coding:utf-8 -*-

import requests
from bs4 import BeautifulSoup

import re
import traceback


def getHTMLText(url,code='utf-8'):
    try:
        r = requests.get(url,timeout=30)
        r.raise_for_status()
        # r.encoding = r.apparent_encoding
        r.encoding = code
        return r.text
    except :
        return ''

def getBookList(uList,url):
    html = getHTMLText(url,'utf-8') 
    soup = BeautifulSoup(html,'html.parser')
    # print (soup.prettify())
    # print (soup.div.attrs)
    # print (soup.div['class'])
    # print ( type(soup.div))
    # print ( soup.a.string)
    # index_name =  soup.find_all('div',class_='index-name')[0]
    # print (index_name.string)

    div_names = []
    div_nums = []
    divs = soup.find_all('div',{'class':'cm-body'})
    for i in divs:
        try:
            div_names.append (i.find('div',{'class':'name'}).string)
            div_nums.append (i.find('div',{'class':'works-num'}).string)
        except:
            continue


if __name__ == '__main__':
    stock_list_url = 'https://read.douban.com/provider/all'
    print ('begin......')
    uList = []
    getBookList(uList,stock_list_url)



