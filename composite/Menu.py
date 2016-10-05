#!/usr/bin/python
#-*-  coding:utf-8  -*-
from MenuComponent import MenuComponent

class Menu(MenuComponent):

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.menuComponents = list()

    def add(self, menuComponent):
        self.menuComponents.append(menuComponent)

    def remove(self, menuComponent):
        self.menuComponents.remove(menuComponent)

    def getChild(self, i):
        return self.menuComponents[i]

    def getName(self):
        return self.name

    def getDescription(self):
        return self.description

    def prints(self):
        print('\n' + self.getName() + ', ' + self.getDescription())
        print('---------------------------------')
        for menuComponent in self.menuComponents:
            menuComponent.prints()
