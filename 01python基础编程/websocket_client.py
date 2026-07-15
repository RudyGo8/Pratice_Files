# -*- coding: utf-8 -*-
"""
@File    : websocket_client
@Project : Practice_Files
@Author  : Rudy
@Date    : 2026/5/20 20:57
@Desc    : 

Copyright (c) 2026 Rudy. All rights reserved.
"""

import asyncio
import websockets


async def main():
    uri = "ws://127.0.0.1:8000/ws"

    async with websockets.connect(uri) as websocket:
        print("连接成功")
        await websocket.send("你好，服务端")


        while True:
            response = await websocket.recv()
            print("收到服务端返回：", response)


if __name__ == "__main__":
    asyncio.run(main())