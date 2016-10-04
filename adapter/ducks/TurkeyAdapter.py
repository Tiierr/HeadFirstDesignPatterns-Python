#!/usr/bin/python
#-*-  coding:utf-8  -*-
from Duck import Duck

class TurkeyAdapter(Duck):

    def __init__(self, turkey):
        self.turkey = turkey

    def quack(self):
        self.turkey.gobble()

    def fly(self):
        for i in range(5):
            self.turkey.fly()
