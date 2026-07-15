# -*- coding: utf-8 -*-
"""
@File    : fastmcp_example
@Project : Practice
@Author  : Rudy
@Date    : 2026/5/15 15:55
@Desc    : 

Copyright (c) 2026 Rudy. All rights reserved.
"""

from fastmcp import FastMCP

# 初始化服务器
mcp = FastMCP("my-first-server")


# 定义工具
@mcp.tool
def get_weather(city: str) -> dict:
    """Get the current weather for a city."""
    # 模拟数据
    weather_data = {
        "new york": {"temp": 72, "condition": "sunny"},
        "london": {"temp": 59, "condition": "cloudy"},
        "tokyo": {"temp": 68, "condition": "rainy"},
    }

    city_lower = city.lower()
    if city_lower in weather_data:
        return {"city": city, **weather_data[city_lower]}
    else:
        return {"city": city, "temp": 70, "condition": "unknown"}




if __name__ == "__main__":
    mcp.run()