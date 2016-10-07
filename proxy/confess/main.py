#!/usr/bin/python
#-*-  coding:utf-8  -*-

from Proxy import Proxy

if __name__ == '__main__':
    p = Proxy("李雷","李白","韩梅梅")
    print(p)
    p.send_book()
    p.send_chocolate()
    p.send_flower()
