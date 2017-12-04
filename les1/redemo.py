#encoding = utf-8

import re

if __name__  == '__main__':
    print('enter')

    # match = re.search(r'[1-9]\d{5}','BIT 430021')
    # if match:
    #     print(match.group(0))


    # match = re.match(r'[1-9]\d{5}','BIT 430021')
    # match = re.match(r'[1-9]\d{5}','430021 BIT ')
    # if match:
    #     print(match.group(0))


    # ls = re.findall(r'[1-9]\d{5}','430021 BIT 100081')
    # if ls:
    #     print(ls)

    # sp = re.split(r'[1-9]\d{5}','BIT430021  NUS100081',maxsplit=1)
    # print (sp)

    # for m in re.finditer(r'[1-9]\d{5}','BIT430021  NUS100081'):
    #     if m:
    #         print(m.group(0))
            

    print(re.sub(r'[1-9]\d{5}','aaaaa','BIT430021  NUS100081'))
