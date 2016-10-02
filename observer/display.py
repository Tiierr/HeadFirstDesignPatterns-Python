#!/usr/bin/python
#-*-  coding:utf8  -*-
from subject import Observer, DisplayElement
from weather import WeatherData

class CurrentConditionsDisplay(Observer,DisplayElement,WeatherData):
    def __init__(self,weatherData):
        super(CurrentConditionsDisplay,self).__init__()
        self.weatherData = weatherData
        weatherData.registerObserver(self)

    # 得到发布中心传送来的消息之后更新数据
    def update(self,temp,humidity,pressure):
        self.temp = temp
        self.humidity = humidity
        self.pressure = pressure
        self.display()

    def display(self):
        print("Current conditions: {0}F degrees and {1}% humidity".format(self.temp, self.humidity))
