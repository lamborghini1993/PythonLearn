# -*- coding:utf-8 -*-
'''
@Author: lamborghini1993
@Date: 2019-09-20 13:36:52
@UpdateDate: 2019-09-20 13:45:25
@Description: 
    python3.7
    https://docs.python.org/zh-cn/3/library/asyncio-task.html
'''

import asyncio


async def main():
    print("Hello")
    await asyncio.sleep(1)
    print("World!")

asyncio.run(main())
