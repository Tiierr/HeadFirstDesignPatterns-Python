#!/usr/bin/python
#-*-  coding:utf8  -*-

class CaffeineBeverage(object):
    def prepareRecipe(self):
        self.boilWater()
        self.brew()
        self.pourInCup()
        if self.customerWantsCondiments():
            self.addCondiments()


    def brew(self):
        pass

    def addCondiments(self):
        pass

    def boilWater(self):
        print('Boiling water')

    def pourInCup(self):
        print('Pouring into cup')

    def customerWantsCondiments(self):
        return True
