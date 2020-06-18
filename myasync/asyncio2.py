# -*- coding:utf-8 -*-
'''
@Author: lamborghini1993
@Date: 2019-09-20 13:36:52
@UpdateDate: 2019-09-20 13:51:56
@Description: 
    python3.7
    https://docs.python.org/zh-cn/3/library/asyncio-task.html
    asyncio.run() 函数用来运行最高层级的入口点
'''

import asyncio
import time


async def say_after(delay: int, what: str):
    await asyncio.sleep(delay)
    print(what)


async def main():
    print(f"started at {time.strftime('%X')}")
    await say_after(1, "Hello")
    await say_after(2, "World")
    print(f"finished at {time.strftime('%X')}")

asyncio.run(main())
