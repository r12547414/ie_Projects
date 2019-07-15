#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by iFantastic on 2019/7/9


class Doctor:

    # 对象级别函数
    def Help(self):
        print("医生治病")
    #要声明一个类级别的函数需要@
    @classmethod
    def eat(cls):
        print("吃饭")

doctor1 = Doctor()
doctor1.Help()

# 类直接调用函数
# TypeError: Help()
# missing 1 required
# positional argument: 'self'
# 缺少一个必要的属性
# Doctor.Help(self=1)

Doctor.eat()
# 类函数，可以通过类和对象调用，对象函数，只能通过对象调用
doctor1.eat()


if __name__ == '__main__':
    pass