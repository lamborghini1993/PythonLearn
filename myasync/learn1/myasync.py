# -*- coding:utf-8 -*-
'''
@Description: 自己实现协成、异步
@Author: lamborghini1993
@Date: 2019-05-27 17:03:55
@UpdateDate: 2019-05-27 20:20:19

https://juejin.im/post/5cc788f351882525166c4abf#heading-6

Task类相当于asyncio.Task。本文的Task依据waiting_until来判断恢复执行时间；asyncio.Task是一个future对象，当asyncio的事件循环检测到这个future对象的状态发生变化的时候，执行相应的逻辑。
sleep()函数相等于asyncio.sleep()。不会阻塞。
SleepingLoop相当于asyncio.BaseEventLoop。SleepingLoop用的是最小堆，asyncio.BaseEventLoop更加复杂，基于future对象，以及 selectors模块等。
'''

import types
import datetime
import heapq
import time


class Task:
    def __init__(self, wait_until, coro):
        self.coro = coro
        self.wait_until = wait_until

    def __eq__(self, other):
        return self.wait_until == other.wait_until

    def __lt__(self, other):
        return self.wait_until < other.wait_until


class SleepingLoop:
    def __init__(self, *coros):
        self._new = coros
        self._waiting = []

    def run_until_complete(self):
        for coro in self._new:
            wait_for = coro.send(None)
            heapq.heappush(self._waiting, Task(wait_for, coro))
        while self._waiting:
            now = datetime.datetime.now()
            task = heapq.heappop(self._waiting)
            if now < task.wait_until:
                delta = task.wait_until - now
                time.sleep(delta.total_seconds())
                now = datetime.datetime.now()
            try:
                wait_until = task.coro.send(now)
                heapq.heappush(self._waiting, Task(wait_until, task.coro))
            except StopIteration:
                pass


@types.coroutine
def sleep(seconds: int):
    now = datetime.datetime.now()
    wait_until = now + datetime.timedelta(seconds=seconds)
    actual = yield wait_until
    return actual - now


async def countdown(label, length, *, delay=0):
    print(label, "waiting", delay, "seconds befroe staring countdown")
    delta = await sleep(delay)
    print(label, "starting after waiting", delta)
    while length:
        print(label, "T-minus", length)
        waited = await sleep(1)
        length -= 1
    print(label, "lift-off")


def main():
    loop = SleepingLoop(
        countdown("A", 5, delay=0),
        countdown("B", 3, delay=2),
        countdown("C", 4, delay=1),
    )
    start = datetime.datetime.now()
    loop.run_until_complete()
    print("time is", datetime.datetime.now()-start)


if __name__ == "__main__":
    main()
