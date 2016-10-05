#!/usr/bin/python
#-*-  coding:utf-8  -*-
from MenuComponent import MenuComponent

class MenuItem(MenuComponent):

    def __init__(self, name, description, vegetarian, price):
        self.name = name
        self.description = description
        self.vegetarian = vegetarian
        self.price = price

    def getName(self):
        return self.name

    def getDescription(self):
        return self.description

    def isVegetarian(self):
        return self.vegetarian

    def getPrice(self):
        return self.price

    def prints(self):
        print('  ' + self.getName(), end='')
        if self.isVegetarian():
            print(' (v)', end='')

        print('  $' + str(self.getPrice()))

        print('     -- ' + self.getDescription())
