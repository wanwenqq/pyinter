#encoding = utf-8
import  requests
from bs4 import BeautifulSoup
import bs4


def getHTMLText(url):
    try:
        r = requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ''


def getUnivList(ulist,html):
    soup = BeautifulSoup(html,'html.parser')
    for tr in soup.find('tbody').children:
        if isinstance(tr,bs4.element.Tag):
            tds = tr('td')
            ulist.append( [tds[0].string,tds[1].string,tds[2].string,tds[3].string] )

def printUnivList(ulist,num):
    tpl = '{0:^6}\t{1:{3}^10}\t{2:^6}'
    print(tpl.format('排名','学校名称','得分',chr(12288)))
    for i in range(num):
        u = ulist[i]
        print(tpl.format(u[0],u[1],u[2],chr(12288)))

if __name__ == '__main__':
    url = 'http://www.zuihaodaxue.com/zuihaodaxuepaiming2016.html'
    respone = getHTMLText(url)
    ulist = []
    getUnivList(ulist,respone)
    printUnivList(ulist,30)
