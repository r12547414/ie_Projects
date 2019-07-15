#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by iFantastic on 2019/7/4

names = input("请输入明星们的名字: \n")
name = input("请输入一个明星的名字：\n")

index = names.find(name)

if index != -1:
    print("找到了%s " % index)
else:
    print("未找到明星名字")



if __name__ == '__main__':
    pass