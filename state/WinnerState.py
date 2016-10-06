#!/usr/bin/python
#-*-  coding:utf8  -*-
from State import State

class WinnerState(State):

    def __init__(self, gumballMachine):
        self.gumballMachine = gumballMachine

    def insertQuarter(self):
        print("Please wait, we're already giving you a Gumball")

    def ejectQuarter(self):
        print("Please wait, we're already giving you a Gumball")

    def turnCrank(self):
        print("Turning again doesn't get you another gumball!")

    def dispense(self):
        print("YOU'RE A WINNER! You get two gumballs for your quarter")
        self.gumballMachine.releaseBall()
        if self.gumballMachine.getCount() == 0:
            self.gumballMachine.setState(self.gumballMachine.getSoldOutState())
        else:
            self.gumballMachine.releaseBall()
            if self.gumballMachine.getCount() > 0:
                self.gumballMachine.setState(self.gumballMachine.getNoQuarterState())
            else:
                print("Oops, out of gumballs!")
                self.gumballMachine.setState(self.gumballMachine.getSoldOutState())

    def __str__(self):
        return "despensing two gumballs for your quarter, because YOU'RE A WINNER!"
