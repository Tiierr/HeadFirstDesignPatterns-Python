#!/usr/bin/python
#-*-  coding:utf-8  -*-
class Light(object):
    def __init__(self, location):
        self.location = location
    def on(self):
        print( self.location + " light is on")

    def off(self):
        print( self.location + " light is off")
