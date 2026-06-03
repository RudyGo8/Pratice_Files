# -*- coding: utf-8 -*-
"""
@File    : tcp_client
@Project : Practice_Files
@Author  : Rudy
@Date    : 2026/6/3 20:15
@Desc    : 

Copyright (c) 2026 Rudy. All rights reserved.
"""
import socket

# 创建一个基于 IPv4 + TCP 的网络通信客户端
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(("127.0.0.1", 9000))

client.send("read_temperature".encode("utf-8"))

# 从服务端接收数据，最多1024
data = client.recv(1024)
print("设备返回：", data.decode("utf-8"))

client.close()