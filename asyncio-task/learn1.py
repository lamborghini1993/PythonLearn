# -*- coding:utf-8 -*-
# Author: xiaohao@corp.netease.com
# Date: 2022-04-13 21:12:37
"""
https://docs.python.org/zh-cn/3.10/library/asyncio-task.html#coroutines

asyncio 提供了三种主要机制
1. asyncio.run() 函数用来运行最高层级的入口点 
"""


import asyncio
import time


async def say_after(delay, why):
    await asyncio.sleep(delay)
    print(why)


async def main1():
    print(f"started 1 at {time.strftime('%X')}")
    await say_after(1, "hello")
    print(f"started 2 at {time.strftime('%X')}")
    await say_after(2, "world")
    print(f"started 3 at {time.strftime('%X')}")

coroutine = main1()  # 协程对象
print(coroutine)
asyncio.run(coroutine)
