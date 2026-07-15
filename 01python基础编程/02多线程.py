# -*- coding: utf-8 -*-
"""
@File    : 02多线程
@Project : Practice_Files
@Author  : Rudy
@Date    : 2026/5/19 15:37
@Desc    : 

Copyright (c) 2026 Rudy. All rights reserved.
"""

# 协程
import asyncio
async def coroutine_1():
    print("Coroutine 1 start")
    await asyncio.sleep(1)  # 模拟一个耗时 1 秒的异步操作
    print("Coroutine 1 end")

async def coroutine_2():
    print("Coroutine 2 start")
    await asyncio.sleep(1)
    print("Coroutine 2 end")

async def main():
    await asyncio.gather(coroutine_1(), coroutine_2())

asyncio.run(main())


# asyncio 异步函数
import asyncio
async def fetch_data():
    print("打印开始获取数据的消息")
    # 使用asyncio.sleep 模拟一个I/O操作(例如网络请求、文件读取等)，
    await asyncio.sleep(2)  # 模拟I/O操作
    print("数据获取完成")
    # 返回一个包含示例数据的字典
    return {"data": "example"}
# 定义一个主异步函数 main
async def main():
    # 使用 await 关键词调用 fetch_data函数，等待其执行完成并获取返回值
    data = await fetch_data()
    # 打印返回的数据
    print(data)
# 使用asyncio.run 运行主异步函数 main
asyncio.run(main())

import threading
import time

def worker():
    print("worked started")
    time.sleep(2)  # 休眠两秒钟
    print("worder finished")

# 创建线程
thread = threading.Thread(target=worker)
# 启动线程
thread.start()
# 等待线程完成
thread.join()

# 多进程
import multiprocessing
import time


def worker():
    print("Worker started")
    time.sleep(2)
    print("Worker finished")


if __name__ == '__main__':
    # 创建进程
    process = multiprocessing.Process(target=worker)
    # 启动进程
    process.start()
    # 等待进程完成
    process.join()