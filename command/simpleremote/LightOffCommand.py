#!/usr/bin/python
#-*-  coding:utf-8  -*-
from Command import Command

class LightOffCommand(Command):
    def __init__(self,light):
        self.light = light

    def excute(self):
        self.light.off()
