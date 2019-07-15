#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by iFantastic on 2019/7/8
# 多继承


class Mao:

    def catchMouse(self):
        print("逮老鼠")

    def eat(self):
        print("猫吃老鼠")


class Ying:

    def fly(self):
        print("飞")

    def eat(self):
        print("鹰吃蛇")


class MaoTouYing(Mao,Ying):
    pass

# 定义对象
mty = MaoTouYing()

mty.catchMouse()
# 调用方法(函数)
mty.fly()

# 两个父类有相同属性，会按照最先的父类属性显示
mty.eat()

if __name__ == '__main__':
    pass