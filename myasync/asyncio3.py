# -*- coding:utf-8 -*-
'''
@Author: lamborghini1993
@Date: 2019-09-20 13:50:31
@UpdateDate: 2020-06-19 15:14:53
@Description: 
    asyncio.create_task() 函数用来并发运行作为 asyncio 任务 的多个协程。
'''

import asyncio
import time


async def say_after(delay: int, what: str):
    await asyncio.sleep(delay)
    print(what)


async def main():
    task1 = asyncio.create_task(say_after(3, "Hello"))
    task2 = asyncio.create_task(say_after(2, "World"))
    print(f"started at 1 {time.strftime('%X')}")
    await task1
    print(f"started at 2 {time.strftime('%X')}")
    await task2
    print(f"finished at 3 {time.strftime('%X')}")

asyncio.run(main())
