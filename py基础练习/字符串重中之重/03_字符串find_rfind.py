#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by iFantastic on 2019/7/4
'''
6.1.	find
find 检测str是否包含在mystr中，如果是返回开始索引值，否则返回-1
6.2.	rfind
rfind 类似于find，不过是从右边开始找。
'''
starts = "郭富城、刘德华、黎明、fzd、刘德华"
# 从左往右找第一个字符串的索引 下标 从0 开始
index = starts.find("郭富城") # 将返回值传给index
print(index)
index = starts.find("刘德华")
print(index)
index = starts.find("大东东")
print(index) #不包含在字符串列表中就返回 -1

# rfind 从右侧往左侧开始找
# 查找到的索引也是从左数的索引
indexindex = starts.rfind("郭富城")
print(indexindex)
indexindex = starts.rfind("刘德华")
print(indexindex)

if __name__ == '__main__':
    pass