# -*- coding:utf-8 -*-
# Author: xiaohao@corp.netease.com
# Date: 2022-04-13 21:37:51
"""
https://docs.python.org/zh-cn/3.10/library/asyncio-task.html#awaitables
"""

import asyncio
import datetime


async def display_date():
    loop = asyncio.get_running_loop()
    print(loop)
    end_time = loop.time() + 5.0
    while True:
        print(datetime.datetime.now())
        if loop.time() >= end_time:
            break
        await asyncio.sleep(1)
    print(loop)

asyncio.run(display_date())
