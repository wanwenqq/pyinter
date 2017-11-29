import requests


def getHTMLText(url):
    try:
        r = requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding  = r.apparent_encoding;
        return r.text[:1000]
    except:
        return 'except'


def getAmazeText(url):
    try:
        kv = {'user-agent':'Mozilla/5.0'}
        r = requests.get(url,header=kv)
        r.raise_for_status()
        r.encoding  = r.apparent_encoding;
        return r.text[:1000]
    except:
        return 'amaze except'

def getBaiduText(url):
    try:
        kv = {'wd':'python'}
        r = requests.get(url,params=kv)
        print(r.request.url())
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text[:1000]
    except:
        return 'baidu except'



if __name__ == '__main__':
    print ('enter')


    # url = 'http://bookan.com.cn'
    # print(getHTMLText(url))


    # url = 'https://item.jd.com/5008395.html'
    url = 'https://www.amazon.cn/dp/B01CG62CCE/ref=cngwdyfloorv2_recs_0?pf_rd_p=05f2b7d6-37ec-49bf-8fcf-5d2fec23a061&pf_rd_s=desktop-2&pf_rd_t=36701&pf_rd_i=desktop&pf_rd_m=A1AJ19PSB66TGU&pf_rd_r=3DHA6B40H74NQ9D21P6F&th=1'
    print (getHTMLText(url))

    # r = requests.get('http://bookan.com.cn')
    # print (r.status_code)
    # print (r.encoding)
    # print (r.apparent_encoding)
    # r.encoding  = 'utf-8'
    # print (r.text)

    # r = requests.head('http://bookan.com.cn')
    # print(r.headers)
    # print(r.text)


    # requets方法
    # get post head put delete options
    # playload = {'key1':'value1','key2':'value2'}
    # r = requests.post('http://httpbin.org/post',data = playload)
    # print(r.text)
