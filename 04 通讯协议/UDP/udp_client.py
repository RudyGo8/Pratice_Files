# -*- coding: utf-8 -*-
"""
@File    : udp_client
@Project : Practice_Files
@Author  : Rudy
@Date    : 2026/6/3 20:48
@Desc    : 

Copyright (c) 2026 Rudy. All rights reserved.
"""

import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 发送数据：先把字符串转换成字节数据
client.sendto('read_status'.encode("utf-8"), ("127.0.0.1", 9001))
# 接收UDP服务端返回数据
data, addr = client.recvfrom(1024)

print('设备返回：', data.decode("utf-8"))

client.close()
