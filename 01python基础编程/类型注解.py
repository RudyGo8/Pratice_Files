# -*- coding: utf-8 -*-
"""
@File    : 类型注解
@Project : Practice_Files
@Author  : Rudy
@Date    : 2026/6/6 20:45
@Desc    : 

Copyright (c) 2026 Rudy. All rights reserved.
"""
# 类型注解起到提示语法作用
a1: int = 123
score: float = 80

name1: list[str] = ["Alice", "Bob", "Charlie"]
name1.append('Rudy')
print(name1)

# 函数类型注解
def circle_area_len(r: float) -> tuple[float, float]:
    return round(3.14 *r *r, 1), round(2*3.14*r, 1)

a1 = circle_area_len(10)
print(a1)