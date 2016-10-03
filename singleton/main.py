#!/usr/bin/python
#-*-  coding:utf8  -*-
from ChocolateBoiler import ChocolateBoiler


if __name__ == '__main__':
    boiler = ChocolateBoiler()
    boiler.fill()
    boiler.boil()
    boiler.drain()

    boiler2 = ChocolateBoiler()
    boiler2.fill()
    boiler2.boil()
    boiler2.drain()

    print(boiler is boiler2)
