#!/usr/bin/python
#-*-  coding:utf-8  -*-

class Tuner(object):

    def __init__(self, description, amplifier):
        self.description = description
        self.amplifier = amplifier

    def on(self):
        print(self.description + ' on')

    def off(self):
        print(self.description + ' off')

    def setFrequency(self, frequency):
        print(self.description + " setting frequency to " + str(frequency))
        self.frequency = frequency

    def setAm(self):
        print(self.description + ' setting AM mode')

    def setFm(self):
        print(self.description + ' setting FM mode')

    def __str__(self):
        return self.description
