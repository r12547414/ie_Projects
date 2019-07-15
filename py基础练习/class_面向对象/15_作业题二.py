#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by iFantastic on 2019/7/9
"""
定义一个网络用户类 要处理的信息有用户ID、用户密码、email地址。
在建立类的实例时 把以上三个信息都作为参数输入
其中用户ID和用户密码是必须的 缺省的email地址，是用户ID加上字符串"@gameschool.com"

判断邮箱是否合法，判断id不能为空的方法
要求定义函数，能获取出用户的个人信息。

"""


class NetUser:

    def __init__(self, id, pwd):
        self.id = id
        self.pwd = pwd
        # 自动初始化
        self.email = id + "@gameschool.com"

    def checkId(self, id):
        if id == None or id == "" or id.strip() == "":
            return False
        return True

    def checkEmail(self, email):
        if email.endswith("@gameschool.com"):
            return True # 为真
        return False

if __name__ == '__main__':
    netUser = NetUser("18", "123")
    # 可以重新定义属性参数,以下定义的就是不合法的
    netUser.id = ""
    netUser.email = "xx"

    # 检查id是否合法
    checkId = netUser.checkId(netUser.id)
    if checkId:
        print("id合法")
    else:
        print("id不合法")
    # 检查email是否合法
    checkEmail = netUser.checkEmail(netUser.email)
    if checkEmail:
        print("邮箱合法")
    else:
        print("邮箱不合法")
