# -*- coding:utf-8 -*-
'''
@Description: 异步爬虫
@Author: lamborghini1993
@Date: 2019-05-27 15:54:22
@UpdateDate: 2019-05-27 16:28:47
'''

import asyncio
import time

import aiohttp

URL = "https://juejin.im/post/5cc4e023e51d45402019428b"


def RunTime(func):
    def _Func():
        start = time.time()
        func()
        print("执行%s共花费%s秒" % (func.__name__, time.time()-start))
    return _Func


async def fetch_async(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            status_code = resp.status
            print(status_code)


# @RunTime  这里不可以加装饰器
async def visit_async():
    tasks = []
    for _ in range(100):
        tasks.append(fetch_async(URL))
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(visit_async())
