#!/usr/bin/python
#-*-  coding:utf8  -*-
from CaffeineBeverage import CaffeineBeverage

class Coffee(CaffeineBeverage):
    def brew(self):
        print('Dripping Coffee through filter')

    def addCondiments(self):
        print('Adding Sugar amd Milk\n')


    def customerWantsCondiments(self):
        self.answer = self.getInput()
        if self.answer.startswith('y'):
            return True
        else:
            return False

    def getInput(self):
        answer = input('Would you like milk and sugar with your coffee (y/n) ?')
        answer = answer.strip()
        if answer == '':
            answer = 'n'
        return answer
