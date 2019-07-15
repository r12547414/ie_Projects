#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by iFantastic on 2019/7/8


class Person(object):

    # 构造函数
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self): # 普通函数
        print("人吃饭")


class Doctor(Person):
    # pass
    def __init__(self, name, age, keshi):
        # super star 父类(超类)
        # 父类的对象
        super().__init__(name, age)
        self.keshi = keshi

    def eat(self): # 重写
        # 如果不想完全废弃父类的对象，想兼容父类的对象内容
        super().eat() # 调用父类函数
        # 函数不能直接调用函数，只有类才可以直接调用函数
        print("%s %d岁，%s医生在医院餐厅中吃饭" %(self.name, self.age, self.keshi))

doctor = Doctor("王大拿", 28 ,"武警空军总") # 构造函数
doctor.eat() # 调用函数，pass 的话 不传参会报错

if __name__ == '__main__':
    pass