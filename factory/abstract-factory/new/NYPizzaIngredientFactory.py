#!/usr/bin/python
#-*-  coding:utf8  -*-
from PizzaIngredientFactory import PizzaIngredientFactory
from ThickCrustDough import ThickCrustDough
from PlumTomatoSauce import PlumTomatoSauce
from MozzarellaCheese import MozzarellaCheese
from BlackOlives import BlackOlives
from Spinach import Spinach
from SlicedPepperoni import SlicedPepperoni
from FrozenClams import FrozenClams

class NYPizzaIngredientFactory(PizzaIngredientFactory):
    def createDough(self):
        print(ThickCrustDough())
        return ThickCrustDough()

    def createSauce(self):
        return PlumTomatoSauce()

    def createCheese(self):
        return MozzarellaCheese()

    def createVeggies(self):
        veggies = [BlackOlives(), Spinach()]
        return veggies

    def createPepperoni(self):
        return SlicedPepperoni()

    def createClam(self):
        return FrozenClams()
