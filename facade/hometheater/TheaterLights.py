#!/usr/bin/python
#-*-  coding:utf-8  -*-

class TheaterLights(object):

    def __init__(self, description):
        self.description = description

    def on(self):
        print(self.description + ' on')

    def off(self):
        print(self.description + ' off')

    def dim(self, level):
        print(self.description + " dimming to " + str(level)  + "%")

    def __str__(self):
        return self.description
