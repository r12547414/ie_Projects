#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by iFantastic on 2019/5/5
import threading
import time

# 子线程   一个程序运行起来以后，一定有一个执行代码的东西，这个东西咱们就称之为
def saySorry():
    print("亲爱的，你错了，你能吃饭了吗？")
    time.sleep(1)

if __name__ == '__main__':
    for i in range(5):
        t = threading.Thread(target=saySorry)
        # 启动线程，即让线程开始执行，主线程
        t.start()
