#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by iFantastic on 2019/6/4
# 导入模块
import xlrd

# table = data.sheets()[0] # 通过索引顺序获取
# table = data.sheets_by_index(0) # 通过索引顺序获取
# table = data.sheet_by_name('Sheet1') # 通过名称获取


def main():
    data =xlrd.open_workbook('E:\\20190511物体体积测试数据.xlsx')
    t1 = data.sheets()[0]
    t2 = data.sheet_by_index(0)
    t3 = data.sheet_by_name('Sheet1')

    print(t1)
    print(t2)
    print(t3)

if __name__ == '__main__':
    main()