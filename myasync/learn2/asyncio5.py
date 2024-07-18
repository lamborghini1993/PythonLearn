# -*- coding:utf-8 -*-
'''
@Author: lamborghini1993
@Date: 2019-09-20 13:58:30
@UpdateDate: 2019-09-20 14:20:25
@Description: 
    并发运行任务
    awaitable asyncio.gather(*aws, loop=None, return_exceptions=False)
'''

import asyncio


async def factorial(name: str, number: int):
    f = 1
    for i in range(2, number + 1):
        print(f"Task {name}:Compute factorial({i})...")
        await asyncio.sleep(1)
        f *= i
    print(f"Task {name}:Compute factorial({number}) = {f}...")


async def main():
    await asyncio.gather(
        factorial("A", 2),
        factorial("B", 3),
        factorial("C", 4),
    )


if __name__ == "__main__":
    asyncio.run(main())
