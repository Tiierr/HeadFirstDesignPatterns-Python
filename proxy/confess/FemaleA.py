#!/usr/bin/python
#-*-  coding:utf-8  -*-

from Female import Female

class FemaleA(Female):
    def __init__(self,name):
        super(FemaleA, self).__init__()
        self.name = name
