#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by iFantastic on 2019/7/3

'''
1.3. 星期判断，输入1-7中任意数字，
根据数字打印当前是星期一。
【如果是7就显示星期日】。
如果输入的数字不再1-7之间提示请重新输入。
'''

while True:
    try:
        num = int(input("请输入1-7中任意数字:\n"))
    except Exception as e:
        print("输入有误")


    if num <1 or num >7:
        print("请重新输入")
    else:
        if num ==1:
            print("星期一")
        elif num ==2:
            print("星期二")
        elif num ==3:
            print("星期三")
        elif num ==4:
            print("星期四")
        elif num ==5:
            print("星期五")
        elif num ==6:
            print("星期六")
        elif num ==7:
            print("星期日")
        else:
            print("输入错误，请重新输入")

if __name__ == '__main__':
    pass