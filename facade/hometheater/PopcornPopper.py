#!/usr/bin/python
#-*-  coding:utf-8  -*-

class PopcornPopper(object):

    def __init__(self, description):
        self.description = description

    def on(self):
        print(self.description + ' on')

    def off(self):
        print(self.description + ' off')

    def pop(self):
        print(self.description + ' popping popcorn!')

    def __str__(self):
        return self.description
