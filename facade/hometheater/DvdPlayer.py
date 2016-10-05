#!/usr/bin/python
#-*-  coding:utf-8  -*-

class DvdPlayer(object):
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

    def play(self, movie):
        self.movie = movie
        print(self.description + " playing '" + self.movie + "'")

    def stop(self):
        print(self.description + " stopped '" + self.movie + "'")

    def pause(self):
        print(self.description + " paused '" + self.movie + "'")

    def setTwoChannelAudio(self):
        print(self.description + ' set two channel audio')

    def setSurroundAudio(self):
        print(self.description + ' set surround audio')

    def __str__(self):
        return self.description
