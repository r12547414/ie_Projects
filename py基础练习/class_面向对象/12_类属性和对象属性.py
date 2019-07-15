#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by iFantastic on 2019/7/8


class Person():
    countrycountry = "中国"

    def __init__(self, name, age):
        self.name = name
        self.age = age

person1 = Person("张三", 19)
person2 = Person("李四", 20)
per1 = person1.countrycountry

print(per1)

per2 = person1.countrycountry = "美国"
print(per2)

per3 = person2.countrycountry
print(per3)
print(Person.countrycountry)

Person.countrycountry = "美国"
print(person2.countrycountry)

print(Person.name) #不能直接类调用属性
# 总结：类的属性，类和对象都可以调用，
# 类修改后，对象跟着修改
# 对象属性：只能通过对象进行调用。各自对象拥有各自的属性。

if __name__ == '__main__':
    pass