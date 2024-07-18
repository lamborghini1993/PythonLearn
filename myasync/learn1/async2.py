import asyncio

async def coroutine_example():
    await asyncio.sleep(3)
    return 'zhihu ID: Zarten'

coro = coroutine_example()

loop = asyncio.get_event_loop()
task = loop.create_task(coro)
print('运行情况：', task)
try:
    print('返回值：', task.result())
except asyncio.InvalidStateError:
    print('task状态未完成，捕获了 InvalidStateError 异常')

loop.run_until_complete(task)
print('再看下运行情况：', task)
print('返回值：', task.result())
loop.close()