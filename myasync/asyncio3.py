# -*- coding:utf-8 -*-
'''
@Author: lamborghini1993
@Date: 2019-09-20 13:50:31
@UpdateDate: 2019-09-20 13:52:51
@Description: 
    asyncio.create_task() 函数用来并发运行作为 asyncio 任务 的多个协程。
'''

import asyncio
import time


async def say_after(delay: int, what: str):
    await asyncio.sleep(delay)
    print(what)


async def main():
    task1 = asyncio.create_task(say_after(1, "Hello"))
    task2 = asyncio.create_task(say_after(2, "World"))
    print(f"started at {time.strftime('%X')}")
    await task1
    await task2
    print(f"finished at {time.strftime('%X')}")

asyncio.run(main())
