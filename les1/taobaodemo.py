#encoding = utf-8
import requests
import re


def getHTMLText(url):
    try:
        r = requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except :
        return ''


def parserHTMLText(ulist,html):
    try:
        plt = re.findall(r'\"view_price\"\:\"[\d\.]*\"',html)
        tlt = re.findall(r'\"raw_title\"\:\".*?\"',html)
        # print(plt)
        for i in range(len(plt)):
            price = eval(plt[i].split(':')[1])
            title = eval(tlt[i].split(':')[1])
            ulist.append([price,title])
    except:
        return

def printuList(ulist):
    tplt = '{:4}\t{:8}\t{:16}'
    print(tplt.format('序号','价格','商品名称'))
    count = 0
    for g in ulist:
        count = count+1
        print(tplt.format(count,g[0],g[1]))



if __name__ == '__main__':
    ulist = []
    depth = 2
    goods = '书包'
    url = 'https://s.taobao.com/search?q='+goods
    


    # 根据url获取html文本
    res = getHTMLText(url)

    # 根据获限的文本信息解析成数组
    parserHTMLText(ulist,res)

    # 格式化打印数据
    printuList(ulist)
