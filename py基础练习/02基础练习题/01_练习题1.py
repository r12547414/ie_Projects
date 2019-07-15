#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by iFantastic on 2019/7/3
'''1.
作业:
1.1.练习上课所有代码
1.2.用户登录案例: 预设用户名，张三，密码123，控制台输入姓名和密码

如果用户名输入错误，提示: 用户名不存在
如果用户名输入正确且密码正确: 显示欢迎您，张三
如果用户名输入正确，密码错误，提示用户名或者密码错误
'''


uersname = '张三'
password = '123'

while True:
    name = input('请输入用户名：\n')
    pwd = input("请输入密码：\n")

    if name != uersname:
        print("用户名不存在")
        continue
    else:
        if name == uersname and password == pwd:
            print("欢迎您，%s" % name)
            break
        else:
            print("用户名或密码错误")
            continue

if __name__ == '__main__':
    pass