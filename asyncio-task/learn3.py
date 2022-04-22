# -*- coding:utf-8 -*-
# Author: xiaohao@corp.netease.com
# Date: 2022-04-13 21:24:26
"""
https://docs.python.org/zh-cn/3.10/library/asyncio-task.html#awaitables

如果一个对象可以在 await 语句中使用，那么它就是 可等待 对象。
可等待 对象有三种主要类型: 协程, 任务 和 Future.
"""


import asyncio

async def nested():
    return 42

# 1. 协程
async def my_coroutine():
    # Nothing happens if we just call "nested()".
    nested()

    # Let's do it differently now and await it:
    print(await nested())  # will print "42".

# 2. 任务
async def my_task():
    task = asyncio.create_task(nested())
    print(await task)

# 3. Futures
async def my_futures():
    """
    Future 是一种特殊的 低层级 可等待对象，表示一个异步操作的 最终结果。
    当一个 Future 对象 被等待，这意味着协程将保持等待直到该 Future 对象在其他地方操作完毕。
    在 asyncio 中需要 Future 对象以便允许通过 async/await 使用基于回调的代码。
    通常情况下 没有必要 在应用层级的代码中创建 Future 对象。
    Future 对象有时会由库和某些 asyncio API 暴露给用户，用作可等待对象:
    """
    await function_that_returns_a_future_object()

    # this is also valid:
    await asyncio.gather(
        function_that_returns_a_future_object(),
        some_python_coroutine()
    )


asyncio.run(my_task())