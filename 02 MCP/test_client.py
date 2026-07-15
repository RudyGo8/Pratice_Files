# -*- coding: utf-8 -*-
"""
@File    : test_client
@Project : Practice
@Author  : Rudy
@Date    : 2026/5/15 16:26
@Desc    : 

Copyright (c) 2026 Rudy. All rights reserved.
"""
import asyncio
from fastmcp import Client
from fastmcp.client.transports.stdio import StdioServerParameters


async def main():


    client = Client("fastmcp_example.py")

    # 连接服务
    async with client:
        # List available tools
        tools = await client.list_tools()
        print("Available tools:")
        for tool in tools:
            print(f"  - {tool.name}: {tool.description}")

        print("\\n" + "=" * 50 + "\\n")

        # 调用天气服务
        result = await client.call_tool(
            "get_weather",
            {"city": "Tokyo"}
        )
        print(f"Weather result: {result}")


if __name__ == "__main__":
    asyncio.run(main())