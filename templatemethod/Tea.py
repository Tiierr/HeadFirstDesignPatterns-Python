#!/usr/bin/python
#-*-  coding:utf8  -*-
from CaffeineBeverage import CaffeineBeverage

class Tea(CaffeineBeverage):
    def brew(self):
        print('Steeping the tea')

    def addCondiments(self):
        print('Adding Lemon \n')


    def customerWantsCondiments(self):
        self.answer = self.getInput()
        if self.answer.startswith('y'):
            return True
        else:
            return False

    def getInput(self):
        answer = input('Would you like Lemon with your tea (y/n) ?')
        answer = answer.strip()
        if answer == '':
            answer = 'n'
        return answer
