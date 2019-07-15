#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by iFantastic on 2019/7/9
"""
请定义一个交通工具(Vehicle)的类其中有:
属性速度(speed)体积(size)等等 方法移动(move())
设置速度(setSpeed(int speed))加速speedUp(),减速speedDown()等等.

最后在main()中实例化一个交通工具对象并通过方法给它初始化speed,size的值并且,
打印出来。另外调用加速减速的方法对速度进行改变。

"""


class Vehicle():

    def __init__(self, speed, size):
        self.speed = speed
        self.size = size

    def move(self):
        print("速度为：%d 公里/小时，长度为：%s的车辆在运行" % (self.speed, self.size))

    # 修改速度
    def setSpeed(self, speed):
        self.speed = speed

    # 加速
    def speedUp(self, speed):
        self.speed = self.speed + speed

    # 减速
    def speedDown(self, speed):
        self.speed = self.speed - speed

    def __str__(self):
        return "速度为：%d 公里/小时，长度为：%s" % (self.speed, self.size)
if __name__ == '__main__':
    car1 = Vehicle(100, "3m")
    print(car1.speed, car1.size)
    print(car1)
    car1.move()
    # 设置速度
    car1.setSpeed(120)
    car1.move()
    # 加速和减速
    car1.speedUp(10)
    car1.move()
    car1.speedDown(10)
    car1.move()