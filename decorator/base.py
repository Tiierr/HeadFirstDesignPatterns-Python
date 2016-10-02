#!/usr/bin/python
#-*-  coding:utf8  -*-

class Beverage(object):

    def __init__(self):
        self.description = 'Unknow Beverage'

    def getDescription(self):
        return self.description

    def cost(self):
        pass

class CondimentDecorator(Beverage):
    def getDescription(self):
        pass
