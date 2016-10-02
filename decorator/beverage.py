#!/usr/bin/python
#-*-  coding:utf8  -*-
from base import Beverage

class Espresso(Beverage):

    def __init__(self):
        self.description = 'Espresso'

    def cost(self):
        return 1.99

class DarkRoast(Beverage):

    def __init__(self):
        self.description = 'Dark Roast Coffee'

    def cost(self):
        return 0.99

class HouseBlend(Beverage):

    def __init__(self):
        self.description = 'House Blend Coffee'

    def cost(self):
        return 0.89
