#!/usr/bin/python
#-*-  coding:utf-8  -*-

class CdPlayer(object):
    def __init__(self, description, amplifier):
        self.description = description
        self.amplifier = amplifier

    def on(self):
        print(self.description + ' on')

    def off(self):
        print(self.description + ' off')

    def eject(self):
        self.title = None
        print(self.description + ' eject')

    def play(self, title):
        self.title = title
        print(self.description + " playing '" + self.title + "'")

    def stop(self):
        print(self.description + ' stopped')

    def pause(self):
        print(self.description + " paused '" + self.title + "'")

    def __str__(self):
        return self.description
