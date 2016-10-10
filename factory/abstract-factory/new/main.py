#!/usr/bin/python
#-*-  coding:utf8  -*-
from NYPizzaStore import NYPizzaStore

if __name__ == '__main__':
    nyStore = NYPizzaStore()

    pizza = nyStore.orderPizza('cheese')
    print(pizza)
    print("Sher ordered a " + pizza.getName() + '\n\n')
