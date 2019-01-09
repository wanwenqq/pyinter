
# -*- coding:utf-8 -*-
# 短链接 62与10进制转换  



baseList = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'

# 10 转 62
def changeBase(n,b):
     x,y = divmod(n,b)
     if x>0:
          return changeBase(x,b) + baseList[y]
     else:
          return baseList[y]


#62 转 10 
def changeToTenBase(s,b):
     sL = list(s)
     sL.reverse()
     result = 0
     for x in range(len(sL)):
          result = result + baseList.index(sL[x])*(b**x)
     return result
