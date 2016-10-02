#!/usr/bin/python
#-*-  coding:utf8  -*-
from subject import Subject

# 继承Subject类
class WeatherData(Subject):

    def __init__(self):
        super(WeatherData,self).__init__()
        self.observers = list()

    def registerObserver(self, observer):
        self.observers.append(observer)

    def removerObserver(self, observer):
        if self.observers.index(observer) >= 0:
            self.observers.remove(observer)

    def notifyObservers(self):
        for obj in self.observers:
            obj.update(self.temp,self.humidity,self.pressure)

    # 获得更新观测值时用来通知观察者
    def measurementsChanged(self):
        self.notifyObservers()

    def setMeasurements(self,temp,humidity,pressure):
        self.temp = temp
        self.humidity = humidity
        self.pressure = pressure
        self.measurementsChanged()
