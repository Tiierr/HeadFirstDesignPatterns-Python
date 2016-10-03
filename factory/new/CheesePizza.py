#!/usr/bin/python
#-*-  coding:utf8  -*-
from Pizza import Pizza
from PizzaIngredientFactory import PizzaIngredientFactory

class CheesePizza(Pizza):
    def __init__(self,ingredientFactory):
        super(CheesePizza,self).__init__()
        self.ingredientFactory = ingredientFactory

    def prepare(self):
        print("Preparing " + self.name)
        self.dough = self.ingredientFactory.createDough()
        self.sauce = self.ingredientFactory.createSauce()
        self.cheese = self.ingredientFactory.createCheese()
