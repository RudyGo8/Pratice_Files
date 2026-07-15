# -*- coding: utf-8 -*-
"""
@File    : 匿名函数
@Project : Practice_Files
@Author  : Rudy
@Date    : 2026/6/6 15:56
@Desc    : 

Copyright (c) 2026 Rudy. All rights reserved.
"""

# 1. map + lambda：对列表每个元素求平方    # 输出: [1, 4, 9, 16, 25]
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)

print('-'*100)

# 2. filter + lambda：筛选列表中的偶数
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers) # 输出: [2, 4, 6, 8]

print('-'*100)

# 3. reduce + lambda：计算列表元素的累积乘积
from functools import reduce
numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)
print(product) # 输出: 120