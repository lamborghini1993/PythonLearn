# -*- coding:utf-8 -*-
# Author: xiaohao@corp.netease.com
# Date: 2022-04-21 17:46:30
"""

"""


import asyncio
import contextvars


async def test():
    tt = contextvars.copy_context()
    print(dir(tt))
    print("test")


async def main():
    tt = contextvars.copy_context()
    print(dir(tt))
    task = asyncio.create_task(test())
    await task


asyncio.run(main())
