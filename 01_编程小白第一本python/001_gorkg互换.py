#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by iFantastic on 2019/6/13

# 设计一个重量转换器，克与千克转换
def g2kg(g):
    return str(g/1000) + "kg"
print(g2kg(2000)) # 调用函数并打印结果

# 设计一个求直角三角形斜边长的函数
# (两条直角边为参数，求最长边)
def Pythongorean_theorem(a, b):
    return 'The right triangle third side\'s length is {}'.format((a**2 + b**2)**(1/2))
# 等价于a的平方与b的平方之和的1/2次方(即开根)
print(Pythongorean_theorem(3,4))# 调用函数并打印结果


# 摄氏度转华摄氏度
def fahrenheit_converter(C):
    fahrenheit = C * 9/5 + 32
    return str(fahrenheit) + '°F'
C2F = fahrenheit_converter(35)
print(C2F)




sum = 0
i = 0
while True:
    if i <= 100:
        sum = sum + i
        i += 1
    else:
        break
print(sum)
# break 跳出循环 continue结束本次，开始下一次循环
# return 返回（结束函数的执行；结束执行并返回数据）

sum2 = 0
for i in range(1,101): # 包头不包尾
    sum2 = sum2 + i
print(sum2)

for a in "for循环求和":
    print(a)

if __name__ == '__main__':
    pass