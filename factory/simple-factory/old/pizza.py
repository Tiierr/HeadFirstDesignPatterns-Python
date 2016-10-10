#!/usr/bin/python
#-*-  coding:utf8  -*-
from base import Pizza

class NYStyleCheesePizza(Pizza):
    def __init__(self):
        super(NYStyleCheesePizza,self).__init__()
        self.name = 'NY Style Sause and Cheese Pizza'
        self.dough = 'Thin Crust Dough'
        self.sauce = 'Marinara Sauce'
        self.toppings.append('      Grated Reggiano Cheese')
        self.toppings.append('      Grated Milk Cheese')

class ChicagoSTyleCheesePizza(Pizza):
    def __init__(self):
        super(ChicagoSTyleCheesePizza,self).__init__()
        self.name = 'Chicago Style Deep Dish Cheese Pizza'
        self.dough = 'Extra Thick Crust Dough'
        self.sauce = 'Plum Tomato Sauce'
        self.toppings.append('      Shredded Mozzarella Cheese')

    def cut(self):
        print('Cutting the pizza into square slices')
