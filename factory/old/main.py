#!/usr/bin/python
#-*-  coding:utf8  -*-
from base import Pizza
from pizza import ChicagoSTyleCheesePizza, NYStyleCheesePizza
from pizzaStore import NYPizzaStore,ChicagoPizzaStore

if __name__ == '__main__':
    nyStore = NYPizzaStore()
    chicagoStore = ChicagoPizzaStore()

    pizza = nyStore.orderPizza('cheese')
    print("Ethan ordered a " + pizza.getName() + '\n\n')

    pizza = chicagoStore.orderPizza('cheese')
    print("Ray ordered a " + pizza.getName())
