# -*- coding:utf-8 -*-
'''
@Author: lamborghini1993
@Date: 2019-09-20 14:37:39
@UpdateDate: 2019-09-20 14:40:37
@Description: 使用异步实现TCP客户端
'''

import asyncio


async def tcp_client(message: str):
    reader, write = await asyncio.open_connection("127.0.0.1", 8008)

    print(f"Send: {message!r}")
    write.write(message.encode())

    data = await reader.read(100)
    print(f"Received: {data.decode()!r}")

    print("Close the connection")
    write.close()

asyncio.run(tcp_client("Hello World!"))
