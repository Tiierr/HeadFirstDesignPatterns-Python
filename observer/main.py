#!/usr/bin/python
#-*-  coding:utf8  -*-
from weather import WeatherData
from display import CurrentConditionsDisplay

if __name__ == '__main__':
    weather = WeatherData()
    currentDisplay = CurrentConditionsDisplay(weather)

    weather.setMeasurements(80,65,20)
    weather.setMeasurements(99,88,220)
