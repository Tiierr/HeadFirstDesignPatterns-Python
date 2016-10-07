#!/usr/bin/python
#-*-  coding:utf-8  -*-

from Male import Male
from FemaleA import FemaleA

class MaleA(Male):
    def __init__(self,name,love_female):
        self.name = name
        self.love_female = FemaleA(love_female)

    def send_flower(self):
        print('%s send flowers to %s.'
                % (self.name,self.love_female.name))

    def send_chocolate(self):
        print('%s send chocolate to %s.'
                % (self.name,self.love_female.name))

    def send_book(self):
        print('%s send books to %s.'
                % (self.name,self.love_female.name))
