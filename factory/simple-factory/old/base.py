#!/usr/bin/python
#-*-  coding:utf8  -*-

class Pizza(object):
    def __init__(self):
        self.toppings = list()

    def prepare(self):
        print('Preparing ' + self.name)
        print('Tossing dough...')
        print('Adding sauce...')
        print('Adding toppings: ')
        for topping in self.toppings:
            print(topping)

    def bake(self):
        print('Bake for 25 minutes at 350')

    def cut(self):
        print('Cutting the pizza into diagonal slices')

    def box(self):
        print('Place pizza in official PizzaStore box')

    def getName(self):
        return self.name

class PizzaStore(object):

    def orderPizza(self,_type):
        self.pizza = self.createPizza(_type)
        self.pizza.prepare()
        self.pizza.bake()
        self.pizza.cut()
        self.pizza.box()

        return self.pizza

    def createPizza(self,_type):
        pass
