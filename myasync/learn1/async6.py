# -*- coding:utf-8 -*-
'''
@Description: 异步 python3.7
@Author: lamborghini1993
@Date: 2019-05-27 15:54:22
@UpdateDate: 2019-05-28 13:32:10
'''

import asyncio


async def heavy_task():
    await asyncio.sleep(2)


async def main():
    for _ in range(100):
        await heavy_task()

if __name__ == '__main__':
    asyncio.run(main())
