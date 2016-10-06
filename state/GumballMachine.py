#!/usr/bin/python
#-*-  coding:utf8  -*-
from SoldState import SoldState
from SoldOutState import SoldOutState
from NoQuarterState import NoQuarterState
from HasQuarterState import HasQuarterState
from WinnerState import WinnerState

class GumballMachine(object):
    def __init__(self,numberGumballs=0):
        self.soldOutState = SoldOutState(self)
        self.noQuarterState = NoQuarterState(self)
        self.hasQuarterState = HasQuarterState(self)
        self.soldState = SoldState(self)
        self.winnerState = WinnerState(self)

        self.count = numberGumballs
        if(numberGumballs > 0):
            self.state = self.noQuarterState

    def insertQuarter(self):
        self.state.insertQuarter()

    def ejectQuarter(self):
        self.state.ejectQuarter()

    def turnCrank(self):
        self.state.turnCrank()
        self.state.dispense()

    def setState(self,state):
        self.state = state

    def releaseBall(self):
        print("A gumball comes rolling out the slot...")
        if self.count > 0:
            self.count = self.count - 1

    def getCount(self):
        return self.count

    def refill(self,count):
        self.count = count
        self.state = self.noQuarterState

    def getState(self):
        return self.state

    def getSoldOutState(self):
        return self.soldOutState

    def getNoQuarterState(self):
        return self.noQuarterState

    def getHasQuarterState(self):
        return self.hasQuarterState

    def getSoldState(self):
        return self.soldState

    def getWinnerState(self):
        return self.winnerState

    def __str__(self):
        result = list()
        result.append("\nMighty Gumball, Inc.")
        result.append("Java-enabled Standing Gumball Model #2004")
        if self.count > 1:
            isComplex = "s"
        else:
            isComplex = ''
        result.append("Inventory: {0} gumball{1}".format(self.count,isComplex))
        result.append("Machine is {0}".format(self.state))
        return '\n'.join(result)
