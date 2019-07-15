#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by iFantastic on 2019/6/24
'''
i = 1

while i <= 9:
    j = 1
    while j <= i: # j<=i 就是三角形
        print("* ",end="")
        j += 1
    print("")
    i += 1
print("程序结束")

i = 1

while i <= 9:
    j = 1
    while j <= 9: # i和j相同就是矩形
        print("* ",end="")
        j += 1
    print("")
    i += 1
print("程序结束")
'''

i = 1

while i <=9:
    # 专门用来打印空格的
    q = 1
    while q <=9-i:
        print("  ", end="")
        q +=1
    j = 1
    while j <=i:
        print("* ", end="")
        j +=1
    s = 1
    while s <=i-1:
        print("* ", end="")
        s +=1

    print("")
    i +=1

if __name__ == '__main__':
    pass