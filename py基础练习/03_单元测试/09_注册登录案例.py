#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by iFantastic on 2019/7/15
# 创建一张表
# User id username password email
# CREATE TABLE USER(id INT PRIMARY KEY AUTO_INCREMENT,username VARCHAR(20),PASSWORD VARCHAR(20),email VARCHAR(20));
# 注册的功能
# 登录的功能
import pymysql


def login():
    pass


def regist():

    # 注册功能
    # 连接数据库
    connect = pymysql.connect(host ="localhost",
                              port =3306,
                              db ="1902a",
                              user ="root",
                              password ="root",
                              charset ="utf8")

    # 获取cursor
    cursor = connect.cursor()
    # 键盘录入
    username = input("请输入姓名：\n")
    password = input("请输入姓名：\n")
    email = input("请输入姓名：\n")

    # 准备sql
    sql = "insert into user VALUES (0,%s,%s,%s)"
    cursor.execute(sql,[username,password,email])
    if num ==1:
        print("注册成功")
    else:
        print("注册失败")
    # 提交
    connect.commit()

    # 关闭
    cursor.close()
    connect.close()



if __name__ == '__main__':

    while True:

        num = int(input("请选择：1 登录 2 注册"))

        if num == 1:
            login() # alt+enter创建类

        elif num == 2:
            regist()
            # 不满足返回循环调条件
            continue

        else:
            print("输入错误")