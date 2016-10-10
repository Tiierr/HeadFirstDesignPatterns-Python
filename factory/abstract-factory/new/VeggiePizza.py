#!/usr/bin/python
#-*-  coding:utf8  -*-
from Pizza import Pizza
from PizzaIngredientFactory import PizzaIngredientFactory

class VeggiePizza(Pizza):
    def __init__(self,ingredientFactory):
        super(VeggiePizza,self).__init__()
        self.ingredientFactory = ingredientFactory

    def prepare(self):
        print("Preparing " + self.name)
        self.dough = self.ingredientFactory.createDough()
        self.sauce = self.ingredientFactory.createSauce()
        self.cheese = self.ingredientFactory.createCheese()
        self.veggies = self.ingredientFactory.createVeggies()
