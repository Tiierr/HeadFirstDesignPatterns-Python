#!/usr/bin/python
#-*-  coding:utf-8  -*-

class CeilingFan(object):
    SPEED = {'HIGH':3,'MEDIUM':2,'LOW':1,'OFF':0}
    def __init__(self, location):
        """
        吊扇的不同状态
        """
        self.HIGH = 3
        self.MEDIUM = 2
        self.LOW = 1
        self.OFF = 0
        self.location = location
        self.speed = self.OFF

    """
    设置吊扇的速度
    """
    def high(self):
        self.speed = self.HIGH
        print(self.location + " ceiling fan is on high")

    def medium(self):
        self.speed = self.MEDIUM
        print(self.location + " ceiling fan is on medium")

    def low(self):
        self.speed = self.LOW
        print(self.location + " ceiling fan is on low")

    def off(self):
        self.speed = self.OFF
        print(self.location + " ceiling fan is off")

    def getSpeed(self):
        return self.speed
