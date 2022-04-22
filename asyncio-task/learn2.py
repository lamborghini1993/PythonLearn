# -*- coding:utf-8 -*-
# Author: xiaohao@corp.netease.com
# Date: 2022-04-13 21:18:59
"""
https://docs.python.org/zh-cn/3.10/library/asyncio-task.html#coroutines

asyncio 提供了三种主要机制
2. asyncio.create_task() 函数用来并发运行作为 asyncio 任务 的多个协程
"""


import asyncio
import time


async def say_after(delay, why):
    await asyncio.sleep(delay)
    print(why)


async def main():
    task1 = asyncio.create_task(say_after(1, "hello"))
    task2 = asyncio.create_task(say_after(2, "world"))

    print(f"started at {time.strftime('%X')}")

    await task1
    print(f"center at {time.strftime('%X')}")
    await task2

    print(f"finished at {time.strftime('%X')}")

    # 预期的输出显示代码段的运行时间比之前快了 1 秒

asyncio.run(main())
