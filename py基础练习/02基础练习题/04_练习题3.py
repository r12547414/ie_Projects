#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by iFantastic on 2019/7/3
"""
1.4. 输入一个100-999之间的数，
判断是否是水仙花数
1 5 3
3*3*3=27
5*5*5=125
1*1*1=1
==========
       153
ge = 153%10=3
十 153 // 10 = 15 % 10 =5
百 = 153 //10 //10%10 =1
"""
num = int(input("输入一个100-999之间的数:\n"))
# 取出个位
ge = num % 10
# 取出十位
shi= num//10%10
# 取出百位
bai = num//10//10%10

cheng = ge ** 3 + shi**3 + bai ** 3
if num == cheng:
    print("%d 是水仙花数" % num)
else:
    print("不是")


# 获取当前所有的水仙花数
for i in range(100, 1000):

    # 取出个位
    ge = i % 10
    # 取出十位
    shi = i // 10 % 10
    # 取出百位
    bai = i // 10 // 10 % 10

    cheng = ge ** 3 + shi ** 3 + bai ** 3
    if i == cheng:
        print("%d 是水仙花数" % i)


if __name__ == '__main__':
    pass