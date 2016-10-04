#!/usr/bin/python
#-*-  coding:utf-8  -*-

class Screen(object):

    def __init__(self, description):
        self.description = description

    def up(self):
        print(self.description + ' up')

    def down(self):
        print(self.description + ' down')

    def __str__(self):
        return self.description
