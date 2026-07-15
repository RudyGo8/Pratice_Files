'''
@create_time: 2026/3/25 下午2:46
@Author: GeChao
@File: 协程.py
'''
import asyncio
import time

start = time.time()


async def task(name):
    print(f"协程 {name} 开始")
    await asyncio.sleep(1)
    print(f"协程 {name} 结束")


async def main():
    await asyncio.gather(task(1), task(2), task(3), task(4))


asyncio.run(main())
# 总耗时：1
print("协程总耗时：", time.time() - start)
