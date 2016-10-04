#!/usr/bin/python
#-*-  coding:utf-8  -*-

class HomeTheaterFacade(object):

    def __init__(self, amp, tuner, dvd, cd,
                projector, screen, lights, popper):
        self.amp = amp
        self.tuner = tuner
        self.dvd = dvd
        self.cd = cd
        self.projector = projector
        self.screen = screen
        self.lights = lights
        self.popper = popper

    def watchMovie(self, movie):
        print("Get ready to watch a movie...")
        self.popper.on()
        self.popper.pop()
        self.lights.dim(10)
        self.screen.down()
        self.projector.on()
        self.projector.wideScreenMode()
        self.amp.on()
        self.amp.setDvd(self.dvd)
        self.amp.setSurroundSound()
        self.amp.setVolume(5)
        self.dvd.on()
        self.dvd.play(movie)

    def endMovie(self):
        print("Shutting movie theater down...")
        self.popper.off()
        self.lights.on()
        self.screen.up()
        self.projector.off()
        self.amp.off()
        self.dvd.stop()
        self.dvd.eject()
        self.dvd.off()

    def listenToCd(self, cdTitle):
        print("Get ready for an audiopile experence...")
        self.lights.on()
        self.amp.on()
        self.amp.setVolume(5)
        self.amp.setCd(self.cd)
        self.amp.setStereoSound()
        self.cd.on()
        self.cd.play(cdTitle)

    def endCd(self):
        print("Shutting down CD...")
        self.amp.off()
        self.amp.setCd(self.cd)
        self.cd.eject()
        self.cd.off()

    def listenToRadio(self, frequency):
        print("Tuning in the airwaves...")
        self.tuner.on()
        self.tuner.setFrequency(frequency)
        self.amp.on()
        self.amp.setVolume(5)
        self.amp.setTuner(self.tuner)

    def endRadio(self):
        print("Shutting down the tuner...")
        self.tuner.off()
        self.amp.off()
