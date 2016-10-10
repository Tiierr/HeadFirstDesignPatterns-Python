#!/usr/bin/python
#-*-  coding:utf8  -*-

from base import PizzaStore
from pizza import NYStyleCheesePizza,ChicagoSTyleCheesePizza

class NYPizzaStore(PizzaStore):
    def createPizza(self, pizza_type):
        if pizza_type == 'cheese':
            pizza = NYStyleCheesePizza()
        elif pizza_type  == 'veggie':
            pizza = NYStyleCheesePizza()
        return pizza

class ChicagoPizzaStore(PizzaStore):
    def createPizza(self, pizza_type):
        if pizza_type == 'cheese':
            pizza = ChicagoSTyleCheesePizza()
        elif pizza_type  == 'veggie':
            pizza = ChicagoSTyleCheesePizza()
        return pizza
