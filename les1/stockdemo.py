#encoding = utf-8


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


def getStockList(uList,stockUrl):
    html = getHTMLText(stockUrl,'GB2312') 
    soup = BeautifulSoup(html,'html.parser')
    a = soup.find_all('a')
    for i in a:
        try:
            href = i.attrs['href']
            uList.append(re.findall(r'[s][hz]\d{6}',href)[0])
        except:
            continue

def getStockInfo(uList,stockUrl,fpath):
    count = 0
    for stock in uList:
        url = stockUrl+stock+'.html'
        html = getHTMLText(url)
        try:
            if html =='':
                continue
            infoDict = {}
            soup = BeautifulSoup(html,'html.parser')
            stockinfo = soup.find('div',attrs={'class':'stock-bets'})
            name = soup.find_all(attrs={'class':'bets-name'})[0]
            infoDict.update({'股票名称':name.text.split()[0]})
            keyList = stockinfo.find_all('dt')
            if len(keyList) == 0:
                continue
            valueList = stockinfo.find_all('dd')
            for i in range(len(keyList)):
                key = keyList[i].text
                val = valueList[i].text
                infoDict[key] = val
            with open(fpath,'a',encoding='utf-8') as f:
                f.write(str(infoDict)+'\n')
                count += 1
                print('\r进度:{}{:.2f}%'.format(name.text.split()[0],count*100/len(uList)),end='')
        except :
            count += 1
            print('\r进度:{}{:.2f}%'.format(name.text.split()[0],count*100/len(uList)),end='')
            traceback.print_exc()
            continue
    return ''




if __name__ == '__main__':
    stock_list_url = 'http://quote.eastmoney.com/stocklist.html'
    stock_info_url = 'https://gupiao.baidu.com/stock/'
    output_file = 'E://baidustock.txt'
    slist = []
    getStockList(slist,stock_list_url)
    getStockInfo(slist,stock_info_url,output_file)
