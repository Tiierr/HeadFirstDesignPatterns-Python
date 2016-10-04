#!/usr/bin/python
#-*-  coding:utf-8  -*-
from Command import Command

class LightOnCommand(Command):
    def __init__(self,light):
        self.light = light

    def excute(self):
        self.light.on()
