#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by iFantastic on 2019/7/4
"""
1.5. 作业二:键盘录入数字,要求满足1-20之间的数，
如果满足就打印，并记录个数，打印满10个就结束。
"""
count = 0

while True:
    num = int(input("请输入1-20之间的数：\n"))
    if num>=1 and num<=20:
        count +=1
        print("满足条件%d" % num)
    else:
        print("不满足条件")

    if count >=10:
        print("到了10个数字")
        break

if __name__ == '__main__':
    pass