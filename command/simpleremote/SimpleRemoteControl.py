#!/usr/bin/python
#-*-  coding:utf-8  -*-

class SimpleRemoteControl(object):
    def setCommand(self, command):
        self.slot = command

    def buttonWasPressed(self):
        self.slot.execute()
