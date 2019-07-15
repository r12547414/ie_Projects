#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by iFantastic on 2019/4/28
import time
import threading


def sing():
    """唱歌5秒钟"""
    for i in range(3):
        print("----正在唱：菊花茶----%d"%i)
        time.sleep(1)

def dance():
    """跳舞 5秒钟"""
    for i in range(3):
        print("----正在跳舞----%d"%i)
        time.sleep(1)





if __name__ == '__main__':

    print('----开始----：%s'%time.ctime())

    t1 = threading.Thread(target=sing)
    t2 = threading.Thread(target=dance)
    t1.start()
    t2.start()

    while True:
        length = len(threading.enumerate())
        print('当前运行的线程数为:%d'%length)
        if length<=1:
            break

        time.sleep(0.5)

