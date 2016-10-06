#!/usr/bin/python
#-*-  coding:utf8  -*-
from State import State

class NoQuarterState(State):

    def __init__(self, gumballMachine):
        self.gumballMachine = gumballMachine

    def insertQuarter(self):
        print('\nYou inserted a quarter')
        self.gumballMachine.setState(self.gumballMachine.getHasQuarterState())

    def ejectQuarter(self):
        print("You haven't inserted a quarter")

    def turnCrank(self):
        print("You turned,but there's no quarter")

    def dispense(self):
        print("You need to pay first")

    def __str__(self):
        return 'waiting for quarter'
