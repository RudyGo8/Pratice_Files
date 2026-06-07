# -*- coding: utf-8 -*-
"""
@File    : write
@Project : Practice_Files
@Author  : Rudy
@Date    : 2026/6/7 21:06
@Desc    : 

Copyright (c) 2026 Rudy. All rights reserved.
"""
from pymodbus.client import ModbusTcpClient

client = ModbusTcpClient("127.0.0.1", port=1502)

if not client.connect():
    print("连接失败")
    exit()

# 写入：把地址 0 改成 999
result = client.write_register(
    address=0,
    value=999,
    device_id=1
)

if result.isError():
    print("写入失败：", result)
else:
    print("写入成功")

# 读回来验证
result = client.read_holding_registers(
    address=0,
    count=2,
    device_id=1
)

if result.isError():
    print("读取失败：", result)
else:
    print("当前寄存器：", result.registers)

client.close()