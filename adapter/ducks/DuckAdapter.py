#!/usr/bin/python
#-*-  coding:utf-8  -*-

from Turkey import Turkey
from random import randint

class DuckAdapter(Turkey):
    """docstring for DuckAdapter."""
    def __init__(self, duck):
        self.duck = duck

    def gobble(self):
        self.duck.quack()

    def fly(self):
        if randint(0,3) == 0 :
            self.duck.fly()
