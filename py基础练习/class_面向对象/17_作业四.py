#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by iFantastic on 2019/7/9
"""
定义一个 汽车的类，定义一个 人的类。
要求汽车中有乘坐的功能，和下车的功能，
并能把当前乘坐的人的信息打印出来。
"""


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Bus:
    # 定义一个集合
    def __init__(self):
        self.list = []

    def goIn(self, person):
        # 将人添加到bus定义的集合中
        self.list.append(person)

    def goOut(self, person):
        # 将人从bus定义的集合中减去
        self.list.remove(person)

    # 打印人的信息
    def printPerson(self):
        for person in self.list:
            print(person.name, person.age)


if __name__ == '__main__':
    person1 = Person("张三", 18)
    person2 = Person("李四", 19)

    # 定义汽车
    bus = Bus()
    # 上车
    bus.goIn(person1)
    bus.printPerson()

    # 第二个人上车
    bus.goIn(person2)
    bus.printPerson()

    # 下车
    bus.goOut(person1)
    bus.printPerson()

    bus.goOut(person2)
    bus.printPerson()
