#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by iFantastic on 2019/6/18


q = ["flower", "flow", "flight"]

def longest_common_head(list_):
    # 用for循环检查每个单词的前若干位，
    # 需循环的次数为最短的那个单词的长度
    for i in range(min([len(word) for word in list_])):
        check = []
        # 把每个单词的第i位都放进check这个列表
        for word in list_:
            check.append(word[i])
        check = set(check)
        # 把列表变成集合后，如果里面元素都一样，长度就会使1，否则就大于1
        if len(check) > 1:
            return list_[0][:i]
    return list_[0][:min([len(word) for word in list_])]

print(longest_common_head(q))

if __name__ == '__main__':
    pass