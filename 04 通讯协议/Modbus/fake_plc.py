# -*- coding: utf-8 -*-
"""
@File    : fake_plc
@Project : Practice_Files
@Author  : Rudy
@Date    : 2026/6/7 20:59
@Desc    : 

Copyright (c) 2026 Rudy. All rights reserved.
"""

from pymodbus.server import StartTcpServer
from pymodbus.simulator import SimData, SimDevice, DataType

# 4 个区块顺序：
# coils, discrete inputs, holding registers, input registers
device = SimDevice(
    id=1,
    simdata=(
        [SimData(address=0, values=[True] + [False] * 99, datatype=DataType.BITS)],
        [SimData(address=0, values=[False] * 100, datatype=DataType.BITS)],
        [SimData(address=0, values=[123, 456] + [0] * 98, datatype=DataType.REGISTERS)],
        [SimData(address=0, values=[0] * 100, datatype=DataType.REGISTERS)],
    )
)

print("模拟 PLC 已启动：127.0.0.1:1502")
print("Holding Register 0 = 123")
print("Holding Register 1 = 456")

StartTcpServer(
    context=[device],
    address=("127.0.0.1", 1502)
)