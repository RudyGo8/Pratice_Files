# -*- coding: utf-8 -*-
"""
@File    : 正则表达式
@Project : Practice_Files
@Author  : Rudy
@Date    : 2026/5/20 14:57
@Desc    : 

Copyright (c) 2026 Rudy. All rights reserved.
"""

import re
import json


def parse_log_file(file_path):
    # 正则表达式匹配日志数据格式
    pattern = r"frame_info_(\d+)_\d+_(\S+)_\d+_(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}): (.*)"

    # 存储解析结果的列表
    parsed_data = []

    # 打开日志文件
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            # 查找符合模式的行
            match = re.search(pattern, line)
            if match:
                # 提取数据
                frame_id = int(match.group(1))
                user_name = match.group(2)
                start_time = match.group(3)
                json_data = match.group(4)

                # 将JSON部分解析为字典
                data_dict = json.loads(json_data)

                # 构造结果
                parsed_data.append({
                    "frame_id": frame_id,
                    "user_name": user_name,
                    "start_time": start_time,
                    "data": data_dict
                })

    return parsed_data


# 测试函数
file_path = r'D:\Edge 缓存下载\编程测试题目\nohup062501.log'  # 替换为实际日志文件路径
parsed_data = parse_log_file(file_path)

# 打印解析结果
for entry in parsed_data:
    print(entry)
