#!/usr/bin/python
#-*-  coding:utf-8  -*-

class Waitress(object):

    def __init__(self, allMenus):
        self.allMenus = allMenus

    def printMenu(self):
        self.allMenus.prints()
