#!/usr/bin/python
#-*-  coding:utf8  -*-

# 主题发布中心
class Subject(object):

    # 注册观察者
    def registerObserver(self, observer):
        pass

    # 删除观察者
    def removeObserver(self, observer):
        pass

    # 当主题状态改变时,该方法被调用,以通知所有的观察者
    def notifyObservers():
        pass

# 观察者
class Observer(object):

    def update(self, temp, humidity, pressure):
        pass

# 显示中心
class DisplayElement(object):

    def display(self):
        pass
