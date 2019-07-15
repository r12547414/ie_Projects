#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by iFantastic on 2019/7/1

def text_create(name, msg):
    desktop_path = 'D:\\'
    full_path = desktop_path + name + '.txt'
    file = open(full_path, 'w')
    file.write(msg)
    file.close()
    print('Done')

text_create('hello', 'hello world')


if __name__ == '__main__':
    pass