# -*- coding: utf-8 -*-
"""
@File    : udp_server
@Project : Practice_Files
@Author  : Rudy
@Date    : 2026/6/3 20:48
@Desc    : 

Copyright (c) 2026 Rudy. All rights reserved.
"""
# UDP 用户数据报协议-无连接+速度快+不保证送达+不保证顺序+开销小
import socket
# 创建一个 IPv4 + UDP 的服务端
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server.bind(("127.0.0.1", 9001))

print("UDP 设备服务已启动...")

while True:
    data, addr = server.recvfrom(1024)

    message = data.decode("utf-8")
    print("收到数据：", message, "来自：", addr)

    if message == "read_status":
        # 因为UDP没有连接，所以每次回复都要指定发给谁，也就是addr
        server.sendto("status=running".encode("utf-8"), addr)
    else:
        server.sendto("unknown command".encode("utf-8"), addr)