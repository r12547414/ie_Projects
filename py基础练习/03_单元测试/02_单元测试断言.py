#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by iFantastic on 2019/7/11
import unittest
from CaculateUtils import CaculateUtils


class CaculateUtils1(unittest.TestCase):

    def setUp(self):

        # 初始化
        utils = CaculateUtils()
        self.utils = utils

    #1-100的加法
    # 等价类和边界值
    # 有效等价类 i=3,j=28
    def testAdd(self):
        num = self.utils.add(30, 1)
        if num == 31:
            print("执行成功")
        else:
            raise Exception("执行失败")

    def testMinus(self):
        num = self.utils.minus(30, 3)

        if num == 27:
            print("执行成功")
        else:
            raise Exception("执行失败")

    def testDefmulity(self):
        num = self.utils.defmulity(20, 10)
        # python中通用的判断方法 bool值 但单元测试中不常用
        # 单元测试中有很多断言
        assert 200 == num, "实际结果和预期结果不一致"

    # 单元测试中，有很多断言 assertEqual assertNotEqual
    def testDivid(self):
        num = self.utils.divide(20, 2)
        self.assertEqual(10, num, "divid实际结果与预期结果不一致")

    # assertTrue assertFalse 是否为真，是否为假
    # 第三次新加的内容
    def testIsEmpty(self):

        #实际结果不为空
        flag = self.utils.isEmpty("啊哈哈")
        # self.assertTrue(flag, "实际结果与预期结果不一致")
        self.assertFalse(flag, "实际结果与预期结果不一致")

    # assertIn assertNotIn 判断是否包含或者不包含
    def testIsIn(self):
        list = self.utils.hasPerson()
        # self.assertIn("林青霞", list, "不包含此美女")
        # 断言这个人不在集合里 结果为真
        self.assertNotIn("林青霞", list, "不包含此美女")

if __name__ == '__main__':
    unittest.main()