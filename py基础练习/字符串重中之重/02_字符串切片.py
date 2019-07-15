#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by iFantastic on 2019/7/4
'''
切片概念：切片是对操作的对象截取一部分的操作，
字符串，列表，元组都支持切片操作。
'''

str1 = '林青霞和张曼玉，我最喜欢王祖贤'
print(str1[0:3]) # 包含头不包含尾
print(str1[-7:]) # 省略结尾
print(str1[::2]) # 省略开头
print(str1[-7::2]) # 最后就是步长
print(str1[::-1]) #反转字符串
if __name__ == '__main__':
    pass