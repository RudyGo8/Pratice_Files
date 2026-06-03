# -*- coding: utf-8 -*-
"""
@File    : subscriber
@Project : Practice_Files
@Author  : Rudy
@Date    : 2026/6/3 21:12
@Desc    : 

Copyright (c) 2026 Rudy. All rights reserved.
"""
# 订阅者
import json
import paho.mqtt.client as mqtt

broker = "broker.emqx.io"
port = 1883
topic = "factory/device001/temperature"

# MQTT 客户端连接 Broker 成功后，自动执行
def on_connect(client, userdata, flags, rc):
    print("MQTT 连接成功")
    client.subscribe(topic, qos=1)

def on_message(client, userdata, msg):
    payload = msg.payload.decode("utf-8")
    data = json.loads(payload)

    print("收到主题：", msg.topic)
    print("设备编号：", data["device_id"])
    print("温度：", data["temperature"])
    print("时间戳：", data["timestamp"])

client = mqtt.Client()

client.on_connect = on_connect
client.on_message = on_message

client.connect(broker, port, 60)
# 一直监听消息
client.loop_forever()