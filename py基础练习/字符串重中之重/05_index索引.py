#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by iFantastic on 2019/7/4
"""
6.3.	index  索引
index 和find一样，如果不在，会报异常
6.4.	rindex
类似于rindex(),不过是从右边开始找
"""
str1 = "哈哈哈呵呵呵啊啊啊"
index_test = str1.index("和") # 值必须全部匹配

print(index_test)
# 字符串不存在 ValueError: substring not found


if __name__ == '__main__':
    pass