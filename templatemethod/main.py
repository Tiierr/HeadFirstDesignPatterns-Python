#!/usr/bin/python
#-*-  coding:utf8  -*-
from Coffee import Coffee
from Tea import Tea

if __name__ == '__main__':
    coffee = Coffee()
    tea = Tea()

    print('Making coffee...')
    coffee.prepareRecipe()

    print('Making tea...')
    tea.prepareRecipe()
