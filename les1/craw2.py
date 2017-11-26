
#coding   = utf-8


# http://blog.csdn.net/c406495762/article/details/59095864

# -*- coding: UTF-8 -*-
from urllib import request
from urllib import parse
import json
import time
import random
import hashlib



if __name__ == "__main__":
    #对应上图的Request URL
    # Request_URL = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=https://www.baidu.com/link'
    Request_URL = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule&sessionFrom='
    #创建Form_Data字典，存储上图的Form Data
    Form_Data = {}
    

    u = 'fanyideskweb'
    d = 'hello'
    f = str(int(time.time()*1000) + random.randint(1,10))
    c = 'rY0D^0\'nM0}g5Mm1z%1G4'

    sign = hashlib.md5((u + d + f + c).encode('utf-8')).hexdigest()


    Form_Data['from'] = 'AUTO'
    Form_Data['to'] = 'AUTO'
    Form_Data['smartresult'] = 'dict'
    Form_Data['client'] = 'fanyideskweb'
    Form_Data['salt'] = f
    Form_Data['sign'] = sign
    Form_Data['i'] = 'hello'
    Form_Data['doctype'] = 'json'
    Form_Data['version'] = '2.1'
    Form_Data['keyfrom'] = 'fanyi.web'
    Form_Data['action'] = 'FY_BY_CLICKBUTTON'
    Form_Data['typoResult'] = 'true'




    #使用urlencode方法转换标准格式
    data = parse.urlencode(Form_Data).encode('utf-8')

    head = {}
    #写入User Agent信息
    head['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
    head['Accept'] = 'application/json, text/javascript, */*; q=0.01'
    head['Content-Type'] = 'application/x-www-form-urlencoded; charset=UTF-8'
    head['Cookie'] = 'OUTFOX_SEARCH_USER_ID_NCOO=1828599095.5449522; UM_distinctid=15d26df9015df6-0378ef9c96367c-8383667-240000-15d26df9016ed9; _qddaz=QD.sw6six.hy87u3.j4wklr2b; _ntes_nnid=88b1ab24a0e5aeb57bd5269f210c8d1a,1503367798284; _ga=GA1.2.294107204.1501548875; _gid=GA1.2.1291781747.1511224902; JSESSIONID=aaaTwYH9GNLDZ8yT4UD-v; SESSION_FROM_COOKIE=fanyiweb; OUTFOX_SEARCH_USER_ID=98302766@59.173.123.68; ___rl__test__cookies=1511254791158'
 #创建Request对象
    # req = request.Request(Request_URL,data, headers=head)


    #传递Request对象和转换完格式的数据
    # response = request.urlopen(req)
    response = request.urlopen(Request_URL,data)
    #读取信息并解码
    html = response.read().decode('utf-8')
    #使用JSON
    translate_results = json.loads(html)
    if translate_results['errorCode'] == 50:
        print ('errorCode 50')
    else:
        
        #找到翻译结果
        translate_results = translate_results['translateResult'][0][0]['tgt']
        #打印翻译信息
        print("翻译的结果是：%s" % translate_results)