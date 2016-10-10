#!/usr/bin/python
#-*-  coding:utf8  -*-

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
