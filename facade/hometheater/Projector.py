#!/usr/bin/python
#-*-  coding:utf-8  -*-

class Projector(object):

    def __init__(self, description, dvdPlayer):
        self.description = description
        self.dvdPlayer = dvdPlayer

    def on(self):
        print(self.description + ' on')

    def off(self):
        print(self.description + ' off')

    def wideScreenMode(self):
        print(self.description + ' in widescreen mode (16x9 aspect ratio)')

    def tvMode(self):
        print(self.description + ' in tv mode (4x3 aspect ratio)')

    def __str__(self):
        return self.description
