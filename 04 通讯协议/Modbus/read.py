# -*- coding: utf-8 -*-
"""
@File    : read
@Project : Practice_Files
@Author  : Rudy
@Date    : 2026/6/7 20:55
@Desc    : 

Copyright (c) 2026 Rudy. All rights reserved.
"""

from pymodbus.client import ModbusTcpClient

client = ModbusTcpClient("127.0.0.1", port=1502)

if not client.connect():
    print("连接失败")
    exit()

result = client.read_holding_registers(
    address=0,
    count=2,
    device_id=1
)

if result.isError():
    print("读取失败：", result)
else:
    print("读取成功：", result.registers)

client.close()