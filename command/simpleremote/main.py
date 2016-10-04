#!/usr/bin/python
#-*-  coding:utf-8  -*-
from SimpleRemoteControl import SimpleRemoteControl
from LightOnCommand import LightOnCommand
from LightOffCommand import LightOffCommand
from Light import Light

if __name__ == '__main__':
    remote = SimpleRemoteControl()
    light = Light()
    lightOn = LightOnCommand(light)
    lightOff = LightOffCommand(light)

    remote.setCommand(lightOn)
    remote.buttonWasPressed()

    remote.setCommand(lightOff)
    remote.buttonWasPressed()
