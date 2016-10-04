#!/usr/bin/python
#-*-  coding:utf-8  -*-
from Amplifier import Amplifier
from Tuner import Tuner
from DvdPlayer import DvdPlayer
from CdPlayer import CdPlayer
from Projector import Projector
from TheaterLights import TheaterLights
from Screen import Screen
from PopcornPopper import PopcornPopper
from HomeTheaterFacade import HomeTheaterFacade

if __name__ == '__main__':
    amp = Amplifier("Top-O-Line Amplifier")
    tuner = Tuner("Top-O-Line AM/FM Tuner", amp)
    dvd = DvdPlayer("Top-O-Line DVD Player", amp)
    cd = CdPlayer("Top-O-Line CD Player", amp)
    projector = Projector("Top-O-Line Projector", dvd)
    lights = TheaterLights("Theater Ceiling Lights")
    screen = Screen("Theater Screen")
    popper = PopcornPopper("Popcorn Popper")

    homeTheater = HomeTheaterFacade(amp, tuner, dvd, cd,
                    projector, screen, lights, popper)

    homeTheater.watchMovie("Raiders of the Lost Ark")
    homeTheater.endMovie()
