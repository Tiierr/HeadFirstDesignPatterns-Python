#!/usr/bin/python
#-*-  coding:utf8  -*-

def singleton(cls):
    instances = {}

    def wrapper(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return wrapper

@singleton
class ChocolateBoiler(object):
    def __init__(self):
        self.empty = True
        self.boiled = False

    def fill(self):
        # fill the boiler with a milk/chocolate mixture
        if self.isEmpty():
            self.empty = False
            self.boiled = False

    def drain(self):
        if not self.isEmpty() and self.isBoiled():
            # drain the boiled milk and chocolate
            self.empty = True

    def boil(self):
        if not self.isEmpty() and not self.isBoiled():
            # bring the contents to a boil
            self.boiled = True

    def isEmpty(self):
        return self.empty

    def isBoiled(self):
        return self.boiled
