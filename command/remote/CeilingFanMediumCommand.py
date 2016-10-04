#!/usr/bin/python
#-*-  coding:utf-8  -*-
from Command import Command
from CeilingFan import CeilingFan

class CeilingFanMediumCommand(Command):
    def __init__(self, ceilingFan):
        self.ceilingFan = ceilingFan

    def execute(self):
        self.prevSpeed = self.ceilingFan.getSpeed()
        self.ceilingFan.medium()

    def undo(self):
        if self.prevSpeed == CeilingFan.SPEED['HIGH']:
            self.ceilingFan.high()
        elif self.prevSpeed == CeilingFan.SPEED['MEDIUM']:
            self.ceilingFan.medium()
        elif self.prevSpeed == CeilingFan.SPEED['LOW']:
            self.ceilingFan.low()
        elif self.prevSpeed == CeilingFan.SPEED['OFF']:
            self.ceilingFan.off()
