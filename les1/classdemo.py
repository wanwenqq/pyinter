# -*- coding:utf-8 -*-

class Animal:
    def __init__(self, can_fly=False):
        self.can_fly = can_fly

    def fly(self):
        if(self.can_fly):
            print('i can fly')
        else:                   
            print('i can not fly')

    def eat(self):
        print('i eat something')

    def __call__(self,name):
        print(name)

class Dog(Animal): #继承
    def bark(self):
        print('woof!')
    
    #重写
    def eat(self):
        print('i eat boune')


# d = Dog(True)
# d.fly()
# d.bark()
# d.eat()

c  =  Animal()
c('dog')