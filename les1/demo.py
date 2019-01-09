# -*- coding:utf-8 -*-

import math
import pickle
import sys

import decroratordemo
import short62_10 as shortchange


def reverse(data):
     for i in range(len(data)-1,0,-1):
          yield data[i]

def f():
     """ return abc"""
     print('-abc') 





if __name__ == '__main__':
     print('demo test')



     print( 9 // 3)
     print( 9 % 3)






     # print(decroratordemo.hello())


     # print(shortchange.changeBase(12345,62))
     # print(shortchange.changeToTenBase('3D7',62))


     # print(f.__doc__)


     # l = [2*x for x in range(10) if x**2 >3]
     # print(l)
     # ll = [(x,y) for x in range(2) for y in range(2)]
     # print(ll)
     # s = {2*x for x in range(10) if x**2 >3}
     # print(s)
     # d = {len(d):d for d in {'python','java','javascrip'}}
     # print(d)
     # ld = {k:v for v,k in d.items()}
     # print(ld)

     # nohtyp = reverse('python')
     # print(nohtyp)
     # for i in nohtyp:
     #      print(i)




     # print('curren python version:' + sys.version_info.__str__())
     # # print(dir(sys.version_info))
     # if(sys.version_info.major<3):
     #      print('less then 3')
     # elif(sys.version_info.major>3):
     #      print('future')
     # else:
     #      print('python 3.x')

     # python = iter('python')
     # print(python)
     # for i in python:
     #      print(i)
