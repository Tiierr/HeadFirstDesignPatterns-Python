#!/usr/bin/python
#-*-  coding:utf-8  -*-
from Command import Command

class MacroCommand(Command):
    """docstring for MacroCommand."""
    def __init__(self, commands):
        self.commands = commands

    def execute(self):
        for i in range(len(self.commands)):
            self.commands[i].execute()
