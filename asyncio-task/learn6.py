# -*- coding:utf-8 -*-
# Author: xiaohao@corp.netease.com
# Date: 2022-04-13 21:50:36
"""
https://docs.python.org/zh-cn/3.10/library/asyncio-task.html#timeouts

等待 aw 可等待对象 完成，指定 timeout 秒数后超时。

如果 aw 是一个协程，它将自动被作为任务调度。

timeout 可以为 None，也可以为 float 或 int 型数值表示的等待秒数。如果 timeout 为 None，则等待直到完成。

如果发生超时，任务将取消并引发 asyncio.TimeoutError.

要避免任务 取消，可以加上 shield()。

此函数将等待直到 Future 确实被取消，所以总等待时间可能超过 timeout。 如果在取消期间发生了异常，异常将会被传播。

如果等待被取消，则 aw 指定的对象也会被取消。
"""

import asyncio
import datetime


async def eternity():
    print(f"eternity start : {datetime.datetime.now()}")
    await asyncio.sleep(10)
    print(f"eternity end : {datetime.datetime.now()}")


async def main():
    try:
        await asyncio.wait_for(eternity(), timeout=1)
    except asyncio.TimeoutError:
        print("timeout")

asyncio.run(main())
