#!/usr/bin/python
#-*-  coding:utf8  -*-
from base import CondimentDecorator

class Mocha(CondimentDecorator):

    def __init__(self,beverage):
        self.beverage = beverage

    def getDescription(self):
        return self.beverage.getDescription() + ', Mocha'

    def cost(self):
        return 0.20 + self.beverage.cost()

class Soy(CondimentDecorator):

    def __init__(self,beverage):
        self.beverage = beverage

    def getDescription(self):
        return self.beverage.getDescription() + ', Soy'

    def cost(self):
        return 0.15 + self.beverage.cost()

class Whip(CondimentDecorator):

    def __init__(self,beverage):
        self.beverage = beverage

    def getDescription(self):
        return self.beverage.getDescription() + ', Whip'

    def cost(self):
        return 0.10 + self.beverage.cost()

class Milk(CondimentDecorator):

    def __init__(self,beverage):
        self.beverage = beverage

    def getDescription(self):
        return self.beverage.getDescription() + ', Milk'

    def cost(self):
        return 0.10 + self.beverage.cost()
