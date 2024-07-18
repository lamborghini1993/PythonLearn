# -*- coding:utf-8 -*-
'''
@Author: lamborghini1993
@Date: 2019-09-20 13:58:30
@UpdateDate: 2019-09-20 14:04:15
@Description: 可等待对象
    可等待 对象有三种主要类型: 协程, 任务 和 Future.
'''

import asyncio


async def nested() -> int:
    """
    协程函数: 定义形式为 async def 的函数;
    协程对象: 调用 协程函数 所返回的对象。
    """
    print("nested")
    return 42


async def main1():
    # nested()  # 如果直接调用nested()，将会抛出异常
    print(await nested())


async def main2():
    """
    任务 被用来设置日程以便 并发 执行协程。
    当一个协程通过 asyncio.create_task() 等函数被打包为一个 任务，该协程将自动排入日程准备立即运行
    
    """
    task = asyncio.create_task(nested())
    print(await task)


if __name__ == "__main__":
    asyncio.run(main1())
