# -*- coding:utf-8 -*-


import os
import shutil
import  glob
import sys
import re
import math
import random
from urllib.request import urlopen
from datetime import date
import zlib
from string import Template
import psutil



# print (os.getcwd())
# print (os.chdir())
# print (os.system('mkdir today'))
# print (dir(os))
# print (help(os))


# shutil.copyfile('main.py','main1.py')



# print (glob.glob('*.py'))


# print (sys.argv)


# print (re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest'))

# print (math.pi)
# print (math.log(1024,2))


# print  (random.random())
# print  (random.randrange(6))
# print (random.choice([1,2,3,4]))
# print (random.sample(range(10),5))

# print (date.today())
# now = date(2003, 12, 2)
# print (now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B."))


# s = b'witch which has which witches wrist watch'
# print (len(s))
# t = zlib.compress(s)
# print (len(t))
# print (zlib.decompress(t))
# print (zlib.crc32(s))



# t = Template('${village}folk send $$10 to $cause.')  
# print (t.substitute(village='Nottingham', cause='the ditch fund'))

# L = ['Bart', 'Lisa', 'Adam']
# for x in L:
#     str =  'Hello,'+x
#     print(str)


# print(psutil.cpu_count(logical=False))

# print(psutil.disk_partitions())
dictsp ={}
str = 'Django 时间与时区设置问题的问题'
for i in str:
    if i in dictsp:
        dictsp[i] += 1
    else:
        dictsp[i] = 1
dict_list=list(dictsp.items())
# print(dict_list)
ll = sorted(dict_list,key=lambda x:x[1],reverse=True)
print(ll)