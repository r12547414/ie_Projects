#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by iFantastic on 2019/7/11
import unittest


class MyTest(unittest.TestCase):

    #声明函数
    def setUp(self):
        # 初始化操作
        print("初始化操作")

    def tearDown(self):
        print("结尾工作，还原操作")

    def testAdd(self):
        print("单元测试执行的函数")

    def TestB(self):
        print("TestB")

    def testHHHHHH(self):
        print("testHHHHHH")

    def xxxHH(self):
        print("xxxHH")

if __name__ == '__main__':
    unittest.main()