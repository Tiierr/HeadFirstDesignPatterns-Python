#!/usr/bin/python
#-*-  coding:utf-8  -*-
from Command import Command
from NoCommand import NoCommand

class RemoteControl(object):
    def __init__(self):
        self.onCommands = list()
        self.offCommands = list()
        self.noCommand = NoCommand()
        self.undoCommand = self.noCommand

        for i in range(7):
            self.onCommands.append(self.noCommand)
            self.offCommands.append(self.noCommand)

    def setCommand(self, slot, onCommand, offCommand):
        self.onCommands[slot] = onCommand
        self.offCommands[slot] = offCommand

    def onButtonWasPressed(self, slot):
        self.onCommands[slot].execute()
        self.undoCommand = self.onCommands[slot]

    def offButtonWasPressed(self, slot):
        self.offCommands[slot].execute()
        self.undoCommand = self.offCommands[slot]

    def undoButtonWasPressed(self):
        self.undoCommand.undo()


    def __str__(self):
        self.results = list()
        self.results.append('\n--------------  ' + 'Remote Control' + '  --------------\n')
        for i in range(len(self.onCommands)):
            self.results.append('[slot ' + str(i) + '] ' + \
            self.onCommands[i].__class__.__name__ + '    ' + \
            self.offCommands[i].__class__.__name__ )
        self.results.append("[undo] " + self.undoCommand.__class__.__name__)
        self.results.append('----------------------------------------------\n')
        return ('\n'.join(self.results))
