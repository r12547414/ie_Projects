#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by iFantastic on 2019/7/11
# 计算器的一个工具类


class CaculateUtils:

    # 声明函数
    # 加
    def add(self, i, j):
        return i + j
    # 减
    def minus(self, i, j):
        return i - j

    def defmulity(self, i, j):
        return i * j

    def divide(self, i, j):
        return i / j

    # 判断是否为空 新加的内容
    def isEmpty(self, str):
        if str == None or str == "" or str.strip() == "":
            return True
        return False

    # 第四次增加新内容 返回集合
    def hasPerson(self):
        list = ["张曼玉", "刘亦菲", "朱茵"]

        return list



if __name__ == '__main__':
    pass