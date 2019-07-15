#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by iFantastic on 2019/7/3
i= 1
while i<=9:
    j=1
    while j<=i:
        print("%d * %d = %d " %(i, j, i*j), end="")
        j +=1
    print("")
    i+=1
if __name__ == '__main__':
    pass