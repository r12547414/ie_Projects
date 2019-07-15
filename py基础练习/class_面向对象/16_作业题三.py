#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by iFantastic on 2019/7/9
"""
创建一个类 为该类定义三个函数 分别执行下列操作
1、传递两个整数值并找出其中较大的一个值
2、传递三个double值并求出其乘积
3、传递两个字符串值并检查其是否相同
4、在main方法中测试函数的调用
"""

class Utils:
    # 求最大值
    def getMax(self, i, j):
        if i >= j:
            return i
        else:
            return j

    # 求乘积
    def getMulity(self, a, b, c):
        return a * b * c

    def isEqual(self, str1, str2):
        return str1 == str2

if __name__ == '__main__':

    utils = Utils()
    print(utils.getMax(10, 20))
    print(utils.getMulity(1, 2, 3))
    print(utils.isEqual("哈哈!", "哈哈!"))