#encoding=utf-8

import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook
import re


wb = Workbook()
# dest_filename = 'yuntu.xlsx'
# ws1 = wb.active
# ws1.title = "云图机构信息"

def download_page(url):
    """获取url地址页面内容"""
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
    }
    data = requests.get(url, headers=headers).content
    return data


def get_li(doc):
        
    soup = BeautifulSoup(doc, 'html.parser')

 
    ol = soup.find('div', id='content_left')
    title = []  # 标题
    desc = []  # 描述
    urls = []  # urls
    for i in ol.find_all('div',class_='result c-container '):
        title_div = i.find('a').get_text()  # 
        if(i.find('div',class_='c-abstract') == None):
            desc_div=''
        else:
            desc_div = i.find('div',class_='c-abstract').get_text()  # 
        if(i.find('div',class_='f13') == None):
            url_div=''
        else:
            if(i.find('div',class_='f13').find(href=True) == None):
                url_div = ''
            else:
                 url_div = i.find('div',class_='f13').find(href=True)['href']
        title.append(title_div)
        desc.append(desc_div)
        urls.append(url_div)
    
    return title,desc,urls

def main():
    uu = 'https://www.baidu.com/s?wd=云图有声图书馆&pn=%d&oq=云图有声图书馆'
    ii=0;
    titles = []
    descs = [] 
    urls = []
    dest_filename = 'xinyu.xlsx'
    ws1 = wb.active
    ws1.title = "新语机构信息"
    while(ii<65):
        n = ii*10
        str = (uu % n)
        print(ii)
        doc = download_page(str)
        title,desc,url  = get_li(doc)
        titles = titles + title
        descs = descs + desc
        urls = urls+url
        ii = ii+1

    for (i,o,m) in zip(titles,descs,urls):
        col_A = 'A%s' % (titles.index(i) + 1)
        col_B = 'B%s' % (titles.index(i) + 1)
        col_C = 'C%s' % (titles.index(i) + 1)
        ws1[col_A] = i
        ws1[col_B] = o
        ws1[col_C] = m
    wb.save(filename=dest_filename)
        


def xinyu():
    uu = 'https://www.baidu.com/s?wd=新语数字图书馆&pn=%d&oq=新语数字图书馆'
    ii=0;
    titles = []
    descs = [] 
    urls = []
    dest_filename = 'xinyu.xlsx'
    ws1 = wb.active
    ws1.title = "新语机构信息"
    while(ii<65):
        n = ii*10
        str = (uu % n)
        print(ii)
        doc = download_page(str)
        title,desc,url  = get_li(doc)
        titles = titles + title
        descs = descs + desc
        urls = urls+url
        ii = ii+1

    for (i,o,m) in zip(titles,descs,urls):
        col_A = 'A%s' % (titles.index(i) + 1)
        col_B = 'B%s' % (titles.index(i) + 1)
        col_C = 'C%s' % (titles.index(i) + 1)
        ws1[col_A] = i
        ws1[col_B] = o
        ws1[col_C] = m
    wb.save(filename=dest_filename)


def yueting():
    uu = 'https://www.baidu.com/s?wd=悦听有声数字图书馆&pn=%d&oq=悦听有声数字图书馆'
    ii=0;
    titles = []
    descs = [] 
    urls = []
    dest_filename = 'yueting.xlsx'
    ws1 = wb.active
    ws1.title = "悦听有声机构信息"
    while(ii<17):
        n = ii*10
        str = (uu % n)
        print(ii)
        doc = download_page(str)
        title,desc,url  = get_li(doc)
        titles = titles + title
        descs = descs + desc
        urls = urls+url
        ii = ii+1

    for (i,o,m) in zip(titles,descs,urls):
        col_A = 'A%s' % (titles.index(i) + 1)
        col_B = 'B%s' % (titles.index(i) + 1)
        col_C = 'C%s' % (titles.index(i) + 1)
        ws1[col_A] = i
        ws1[col_B] = o
        ws1[col_C] = m
    wb.save(filename=dest_filename)

if __name__  == '__main__':
    # main()
    # xinyu()
    yueting()