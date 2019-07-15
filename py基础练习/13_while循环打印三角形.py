#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by iFantastic on 2019/7/3
# 矩形和三角形只需要改变j<=9就是矩形
i = 1
while i<=9:
    j=1
    while j<=i:
        print("* ",end = "")
        j+=1
    print("")
    i+=1
print("程序结束")

if __name__ == '__main__':
    pass