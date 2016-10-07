#!/usr/bin/python
#-*-  coding:utf-8  -*-

from Male import Male
from MaleA import MaleA

class Proxy(Male):

    def __init__(self, name, proxyed_name, love_female):
        self.name = name
        self.love_female = love_female
        self.proxyed = MaleA(proxyed_name,love_female)

    def send_flower(self):
        self.proxyed.send_flower()

    def send_chocolate(self):
        self.proxyed.send_chocolate()

    def send_book(self):
        self.proxyed.send_book()

    def __str__(self):
        return ('Intro: %s has a crash on %s,but %s too shy to confess in person.\n' % (self.name,self.love_female,self.name))
