# -*- coding:utf-8 -*-
'''
@Author: lamborghini1993
@Date: 2019-09-20 13:36:52
@UpdateDate: 2020-06-19 01:53:47
@Description: 
    python3.7
    https://docs.python.org/zh-cn/3/library/asyncio-task.html
    asyncio.run() 函数用来运行最高层级的入口点
'''

import asyncio
import time


async def say_after(delay: int, what: str):
    await asyncio.sleep(delay)
    return what


async def main():
    print(f"started at {time.strftime('%X')}")
    a1 = await say_after(1, "Hello")
    a2 = await say_after(2, "World")
    print(f"{a1} {a2} finished at {time.strftime('%X')}")

asyncio.run(main())
