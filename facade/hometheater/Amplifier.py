#!/usr/bin/python
#-*-  coding:utf-8  -*-

class Amplifier(object):
    def __init__(self, description):
        self.description = description

    def on(self):
        print(self.description + ' on')

    def off(self):
        print(self.description + ' off')

    def setStereoSound(self):
        print(self.description + ' stereo mode on')

    def setSurroundSound(self):
        print(self.description + " surround sound on (5 speakers, 1 subwoofer)")


    def setVolume(self, level):
        print(self.description + " setting volume to " + str(level))

    def setTuner(self, tuner):
        print(self.description + " setting tuner to " + str(dvd))
        self.tuner = tuner

    def setDvd(self, dvd):
        print(self.description + " setting DVD player to " + str(dvd))
        self.dvd = dvd

    def setCd(self, cd):
        print(self.description + " setting CD player to " + str(cd))
        self.cd = cd

    def __str__(self):
        return self.description
