# -*- coding:utf-8 -*-

import math

import pickle

if __name__ == '__main__':
     # print(hasattr('12','lower'));
     # for i in range(10000):
     #      x = int(math.sqrt(i+100))
     #      y = int(math.sqrt(i+268))

     #      if(x*x ==i +100) and (y*y== i+268):
     #           print(i)
     data = ['1','2' ,'bb', '===cc']  
     p_str = pickle.dumps(data)
     print(p_str)  
     ser_p =  pickle.loads(p_str)
     print(ser_p)