# -*- coding:utf-8 -*-
# Author: xiaohao@corp.netease.com
# Date: 2022-04-14 19:14:14
"""
https://docs.python.org/zh-cn/3.8/library/asyncio-task.html#task-object
"""

import asyncio
import datetime


async def cancel_me():
    print(f'cancel_me(): before sleep {datetime.datetime.now()}')

    try:
        # Wait for 1 hour
        await asyncio.sleep(3600)
    except asyncio.CancelledError:
        print(f'cancel_me(): cancel sleep {datetime.datetime.now()}')
        raise
    finally:
        print(f'cancel_me(): after sleep {datetime.datetime.now()}')

async def main():
    # Create a "cancel_me" Task
    task = asyncio.create_task(cancel_me())

    # Wait for 1 second
    await asyncio.sleep(1)

    task.cancel()
    try:
        await task
    except asyncio.CancelledError:
        print(f"main(): cancel_me is cancelled now {datetime.datetime.now()}")

asyncio.run(main())
