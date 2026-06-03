# -*- coding: utf-8 -*-
"""
@File    : publisher
@Project : Practice_Files
@Author  : Rudy
@Date    : 2026/6/3 21:10
@Desc    : 

Copyright (c) 2026 Rudy. All rights reserved.
"""
# MQTT发布端程序
import json
import time
import random
import paho.mqtt.client as mqtt

# 服务器地址-类似消息中转站
broker = "broker.emqx.io"
port = 1883
# 消息分类路径：订阅这个主题的人，就可以收到这台设备的温度数据
topic = "factory/device001/temperature"

client = mqtt.Client()
# broker 服务器地址，keepalive为心跳时间：60s
client.connect(broker, port, 60)

while True:
    # 构造数据
    data = {
        "device_id": "device001",
        "temperature": round(random.uniform(24, 30), 2),
        "timestamp": int(time.time())
    }

    payload = json.dumps(data)

    # 发布消息，qos=1 至少发布一次，0为最多发布一次，2为只发送一次
    client.publish(
        topic=topic,
        payload=payload,
        qos=1
    )

    print("已发布：", payload)

    time.sleep(5)