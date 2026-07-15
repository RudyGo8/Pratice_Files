# -*- coding: utf-8 -*-
"""
@File    : SSE
@Project : Practice_Files
@Author  : Rudy
@Date    : 2026/5/20 20:20
@Desc    : 

Copyright (c) 2026 Rudy. All rights reserved.
"""

import uvicorn
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
import asyncio
import json
import time

app = FastAPI()

async def sse_event_generator():
    for i in range(10):
        data = {
            "index": i,
            "message": f"这是第{i} 条SSE消息",
            "time": time.strftime('%Y-%m-%d %H:%M:%S')
        }
        # 生成器：一条一条生产数据
        yield f"data:{json.dumps(data, ensure_ascii=False)}\n\n"

        await asyncio.sleep(1)

    yield f"data: {json.dumps({'message': '任务完成'}, ensure_ascii=False)}\n\n"



@app.get("/sse")
async def sse_endpoint():
    # 流式响应
    return StreamingResponse(
        sse_event_generator(),
        # SSE响应头
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "X-Accel-Buffering": "no",
        }
    )

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)