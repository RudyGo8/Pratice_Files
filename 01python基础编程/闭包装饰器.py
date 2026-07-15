# -*- coding: utf-8 -*-
"""
@File    : 闭包
@Project : Practice_Files
@Author  : Rudy
@Date    : 2026/6/6 21:22
@Desc    : 

Copyright (c) 2026 Rudy. All rights reserved.
"""

# 闭包
def func():
    x = 10

    def func2():
        nonlocal x
        x += 1
        return x
    return func2

num1 = func()
print(num1())
print(num1())

# 装饰器

# 需求：在发表评论前，都是需要登录的
# 1. 定义外部函数，形参列表接收要被装饰的函数名(对象)

# 2.定义函数，表示 发表评论
def comment():
    print('this is a comment')
def payment():
    print('this is a payment')



# 3.测试
comment()