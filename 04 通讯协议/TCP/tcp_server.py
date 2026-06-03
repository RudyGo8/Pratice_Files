# -*- coding: utf-8 -*-
"""
@File    : tcp
@Project : Practice_Files
@Author  : Rudy
@Date    : 2026/6/3 20:13
@Desc    : 

Copyright (c) 2026 Rudy. All rights reserved.
"""
# TCP:传输控制协议-面向连接+可靠传输+有顺序+有确认机制+保证可靠性速度慢一点
import socket

# 创建一个基于 IPv4 + TCP 的服务器
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(("127.0.0.1", 9000))
# 监听：开始等待客户端连接，最多一个
server.listen(1)

print("TCP 设备服务已启动，等待连接...")

# 开始连接客户端，成功连接会返回通信对象和地址
conn, addr = server.accept()
print("客户端连接：", addr)

while True:
    data = conn.recv(1024)

    if not data:
        break

    message = data.decode("utf-8")
    print("收到数据：", message)

    if message == "read_temperature":
        conn.send("temperature=26.5".encode("utf-8"))
    else:
        conn.send("unknown command".encode("utf-8"))

conn.close()
server.close()