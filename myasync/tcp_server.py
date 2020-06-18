# -*- coding:utf-8 -*-
'''
@Author: lamborghini1993
@Date: 2019-09-20 14:41:05
@UpdateDate: 2019-09-20 14:47:11
@Description: 使用异步实现TCP服务端
'''

import asyncio


async def handle_echo(reader, writer):
    data = await reader.read(100)
    message = data.decode()
    addr = writer.get_extra_info("peername")

    print(f"Received {message!r} from {addr!r}")
    print(f"Send:{message!r}")
    writer.write(data)
    await writer.drain()
    print(f"Close {addr!r} client connect!")
    writer.close()


async def main():
    server = await asyncio.start_server(handle_echo, "127.0.0.1", 8008)
    addr = server.sockets[0].getsockname()
    print(f"Serving on {addr}")
    async with server:
        await server.serve_forever()


asyncio.run(main())
