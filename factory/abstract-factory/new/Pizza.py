#!/usr/bin/python
#-*-  coding:utf8  -*-
class Pizza(object):

    def __init__(self):
        self.sauce = None
        self.dough = None
        self.cheese = None
        self.veggies = None
        self.clam = None
        self.pepperoni = None

    def prepare(self):
        pass

    def bake(self):
        print('Bake for 25 minutes at 350')

    def cut(self):
        print('Cutting the pizza into diagonal slices')

    def box(self):
        print('Place pizza in official PizzaStore box')

    def setName(self,name):
        self.name = name

    def getName(self):
        return self.name

    def __str__(self):
        self.result = list()
        self.result.append("\n---- " + self.name + " ----\n")
        if self.sauce:
            self.result.append(self.sauce)
        if self.dough:
            self.result.append(self.dough)
        if self.cheese:
            self.result.append(self.cheese)
        if self.veggies:
            s = ' + '.join('%s' % s for s in self.veggies)
            self.result.append(s)
        if self.clam:
            self.result.append(self.clam)
        if self.pepperoni:
            self.result.append(self.pepperoni)
        self.result.append("\n----------------------------------------\n")

        return '\n'.join('%s' % s for s in self.result)
