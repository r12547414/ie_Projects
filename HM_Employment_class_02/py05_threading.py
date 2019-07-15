#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by iFantastic on 2019/5/14
import threading
from time import sleep

def test1():
    for i in range(5):
        print("-----test1-----%d---" % i)
        sleep(1)
    # 如果创建Thread时执行的函数，运行结束那么意味着，这个子线程结束了......


def test2():
    for i in range(5):
        print("-----test2-----%d---" % i)
        sleep(1)


def main():
    t1 = threading.Thread(target=test1)
    t2 = threading.Thread(target=test2)


    t1.start()
    sleep(1)
    print("----1----")
    t2.start()
    sleep(1)
    print("----2----")

    while True:
        print(threading.enumerate())

if __name__ == '__main__':
    main()