#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by iFantastic on 2019/5/29


from tkinter import * # 导入tkinter库

root = Tk()           # 创建窗口对象的背景色
                      # 创建两个列表
li = ['C', 'python', 'php', 'html', 'SQL', 'java']
movie = ['css', 'jQuery', 'Bootstrap']
listb = Listbox(root)  # 传建两个列表组建
listb2 = Listbox(root)

for item in li:        # 第一个小部件插入数据
    listb.insert(0, item)

for item in movie:
    listb2.insert(0, item)

listb.pack()           # 将小部件放置到主窗口中
listb2.pack()
root.mainloop()         # 进入消息循环


if __name__ == '__main__':
    pass