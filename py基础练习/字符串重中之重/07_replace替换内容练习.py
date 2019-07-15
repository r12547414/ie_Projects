#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by iFantastic on 2019/7/4

name1 = "拉"
name2 = "拉里拉"
name3 = "拉,里:拉,里"
names1 =name1.count("拉")
names2 =name2.count("拉里拉")
names3 =name3.count("拉里拉里")
print(names1, names2, names3)

# 把mystr中的str1 替换成str2，如果count指定，则替换不超过count次
# 把第一个参数是要替换的内容，第二个参数替换成的内容

str1 = name3.replace(",", ":")
print(str1)

if __name__ == '__main__':
    pass