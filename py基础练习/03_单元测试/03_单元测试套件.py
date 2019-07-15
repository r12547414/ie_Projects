#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by iFantastic on 2019/7/12
import unittest

if __name__ == '__main__':
    # 第一步：创建单元测试套件的对象
    testSuite = unittest.TestSuite()
    # 第二步：通过testloader加载单元测试类
    unittest.TestLoader().loadTestsFromTestCase(Mytest)