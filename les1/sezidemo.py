#-*- coding:utf-8 -*-

import random

if __name__ == "__main__":
    while True:
        man = int(input('input 3 to 18:'))
        if (man == 0):
            exit(0)
        a = random.randint(1,6)
        b = random.randint(1,6)
        c = random.randint(1,6)

        sum  =  a+b+c
        print(sum)
        if(sum <11 and man <11):
            print('less win')
        elif( sum>10 and man>10):
            print('max win')
        else:
            print('lose')
