import asyncio


async def coroutine_example(name):
    print("开始执行%s" % name)
    await asyncio.sleep(1)
    print("执行%s完毕" % name)


loop = asyncio.get_event_loop()
tasks = [coroutine_example("Test"+str(x)) for x in range(4)]
print(tasks)
wait_coro = asyncio.wait(tasks)
loop.run_until_complete(wait_coro)
print(tasks)
print(wait_coro)
loop.close()
