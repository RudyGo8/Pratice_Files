# -*- coding: utf-8 -*-
"""
@File    : 深拷贝与浅拷贝
@Project : Practice_Files
@Author  : Rudy
@Date    : 2026/5/30 14:16
@Desc    : 

Copyright (c) 2026 Rudy. All rights reserved.
"""
import copy

# lst1 = []
#
# # 变量赋值
# def func1():
#     lst1.append("A")
#
# func1()
# print(f"变量赋值示例：\n lst1:{lst1}")

# 浅拷贝
# lst2 = []
# def func2():
#     copy_lst = lst2.copy()
#     copy_lst.append("B")
#     return copy_lst
#
# new_lst = func2()
# print(new_lst)
# print(lst2)

# 深拷贝，嵌套列表场景
lst3 = [[1, 2], [3, 4]]
def func3():
    copy_lst = copy.deepcopy(lst3)
    copy_lst[0].append(88)
    return copy_lst
new_lst = func3()
print(new_lst)
