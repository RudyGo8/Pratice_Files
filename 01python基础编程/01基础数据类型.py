# -*- coding: utf-8 -*-
"""
@File    : 01基础数据类型
@Project : Practice
@Author  : Rudy
@Date    : 2026/5/10 16:25
@Desc    : 

Copyright (c) 2026 Rudy. All rights reserved.
"""

'''
可变数据类型: 数字、字符串、布尔、元组
不可变数据类型: 列表、字典、集合
'''
 
list1 = ["a", "b", "c", "d"]
print(f"列表示例:{list1}")
# new_list = [name.upper() for name in list1 if len(name)]
# print(f"列表推导式示例:{new_list}\n{'-'*100}")
list2 = [1,2,3,'a','b','c','d']
new_list = [*list1, *list2]
print(new_list)



# tup1 = "a", "b", "c", "d"
# print(f"元组示例:{tup1}")
# new_tup = tuple(x for x in tup1)
# print(f"元祖推导式示例:{new_tup}\n{'-'*100}")
#
# dict1 = {"Google": 1, "ChatGpt": 2, "DeepSeek": 3}
# print(f"字典示例:{dict1}")
# new_dict = {key:value for key, value in dict1.items()}
# print(f"字典推导式示例:{new_dict}\n{'-'*100}")
#
# thisset = {"Dog", "Cat", "Fish"}
# print(f"集合示例:{thisset}")
#
# new_thisset = {x for x in thisset}
# print(f"集合推导式示例:{new_thisset}")








