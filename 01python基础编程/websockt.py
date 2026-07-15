# -*- coding: utf-8 -*-
"""
@File    : websockt
@Project : Practice_Files
@Author  : Rudy
@Date    : 2026/5/20 20:50
@Desc    : 

Copyright (c) 2026 Rudy. All rights reserved.
"""
import uvicorn
import asyncio
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
import json
import time

app = FastAPI()

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    # 1. 接受客户端连接
    await websocket.accept()

    try:
        count = 0
        while True:
            # 2. 接收客户端发来的消息
            message = await websocket.receive_text()

            print("收到客户端消息:", message)

            # 3. 构造服务端响应
            data = {
                "client_message": message,
                "server_message": f"服务端已收到：{message}",
                "time": time.strftime("%H:%M:%S")
            }

            # 4. 发送消息给客户端
            await websocket.send_text(json.dumps(data, ensure_ascii=False))
            count += 1
            await asyncio.sleep(1)

    except WebSocketDisconnect:
        print("客户端断开连接")

if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000)