#!/usr/bin/python
#-*-  coding:utf8  -*-
from PizzaStore import PizzaStore
from NYPizzaIngredientFactory import NYPizzaIngredientFactory
from CheesePizza import CheesePizza
from VeggiePizza import VeggiePizza

class NYPizzaStore(PizzaStore):
    def createPizza(self,item):
        self.ingredientFactory = NYPizzaIngredientFactory()

        if item == 'cheese':
            self.pizza = CheesePizza(self.ingredientFactory)
            self.pizza.setName("New York Style Cheese Pizza")
        elif item == 'veggie':
            self.pizza = VeggiePizza(self.ingredientFactory)
            self.pizza.setName("New York Style Veggie Pizza")

        return self.pizza
