# -*- coding: utf-8 -*-
"""
@File    : 面向对象
@Project : Practice_Files
@Author  : Rudy
@Date    : 2026/6/6 21:09
@Desc    : 

Copyright (c) 2026 Rudy. All rights reserved.
"""
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        print('Car 类型的对象初始化完毕，对象属性已经添加完毕')

    # 魔法方法
    def __str__(self):
        return f'{self.make} {self.model} {self.year}'
    def __eq__(self, other):
        return self.make == other.make and self.model == other.model and self.year == other.year
    def __lt__(self, other):
        return self.make < other.make and self.model < other.model and self.year < other.year


# 创建实例
c1 = Car('2026',"Tesla",1)
print(c1.__dict__)

