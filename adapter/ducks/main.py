#!/usr/bin/python
#-*-  coding:utf-8  -*-
from MallardDuck import MallardDuck
from WildTurkey import WildTurkey
from TurkeyAdapter import TurkeyAdapter


def testDuck(duck):
    duck.quack()
    duck.fly()

if __name__ == '__main__':
    duck = MallardDuck()
    turkey = WildTurkey()
    turkeyAdapter = TurkeyAdapter(turkey)

    print("The Turkey says...")
    turkey.gobble()
    turkey.fly()

    print("\nThe Duck says...")
    testDuck(duck)

    print("\nThe TurkeyAdapter says...")
    testDuck(turkeyAdapter)
