#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by iFantastic on 2019/7/4

str1 = '今天是个好日子，明天依然是好日子a'
print(str1[4],str1[-4])
print(str1[4:7],str1[-4:-1])

for i in str1:
    print(i, end ="")

# for循环形式
for i in range(0, len(str1)):
    print("%d 索引处的字符是 %s " % (i, str1[i]))

if __name__ == '__main__':
    pass