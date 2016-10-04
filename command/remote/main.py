#!/usr/bin/python
#-*-  coding:utf-8  -*-
from RemoteControl import RemoteControl
from LightOnCommand import LightOnCommand
from LightOffCommand import LightOffCommand
from Light import Light

if __name__ == '__main__':
    remote = RemoteControl()
    light = Light('Living room')
    lightOn = LightOnCommand(light)
    lightOff = LightOffCommand(light)

    remote.setCommand(0,lightOn,lightOff)

    remote.onButtonWasPressed(0)
    remote.offButtonWasPressed(0)
    print(remote)

    remote.undoButtonWasPressed()
    remote.offButtonWasPressed(0)
    remote.onButtonWasPressed(0)
    print(remote)

    remote.undoButtonWasPressed()
