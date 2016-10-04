#!/usr/bin/python
#-*-  coding:utf-8  -*-
from RemoteControl import RemoteControl
from CeilingFan import CeilingFan
from CeilingFanHighCommand import CeilingFanHighCommand
from CeilingFanMediumCommand import CeilingFanMediumCommand
from CeilingFanOffCommand import CeilingFanOffCommand

if __name__ == '__main__':
    remoteControl = RemoteControl()
    ceilingFan = CeilingFan('Living Room')
    ceilingFanHigh = CeilingFanHighCommand(ceilingFan)
    ceilingFanMedium = CeilingFanMediumCommand(ceilingFan)
    ceilingFanOff = CeilingFanOffCommand(ceilingFan)

    remoteControl.setCommand(0,ceilingFanHigh,ceilingFanOff)
    remoteControl.setCommand(1,ceilingFanMedium,ceilingFanOff)

    remoteControl.onButtonWasPressed(0)
    remoteControl.offButtonWasPressed(0)
    print(remoteControl)
    remoteControl.undoButtonWasPressed()

    remoteControl.onButtonWasPressed(1)
    print(remoteControl)
    remoteControl.undoButtonWasPressed()
