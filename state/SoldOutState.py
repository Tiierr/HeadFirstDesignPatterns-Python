#!/usr/bin/python
#-*-  coding:utf8  -*-
from State import State

class SoldOutState(State):

    def __init__(self, gumballMachine):
        self.gumballMachine = gumballMachine

    def insertQuarter(self):
        print("\nYou can't insert a quarter, the machine is sold out")

    def ejectQuarter(self):
        print("You can't eject, you haven't inserted a quarter yet")

    def turnCrank(self):
        print("You turned, but there are no gumballs")

    def dispense(self):
        print("No gumball dispensed")

    def __str__(self):
        return 'sold out'
