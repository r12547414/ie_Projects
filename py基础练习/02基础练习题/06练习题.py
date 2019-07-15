#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by iFantastic on 2019/7/4
"""
1.6. 面试题目:1块钱1瓶水，2个瓶盖换一瓶水，
用程序实现输入钱数，得到水的个数
1 1
2 2+1
3 3+1+1   5
4 4+1+1+1  7
。。。。。。
"""
while True:
    money = int(input("请输入钱数：\n"))
    connt = 2 * money - 1
    print("水的个数是 %d" % connt)




if __name__ == '__main__':
    pass