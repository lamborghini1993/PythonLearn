import asyncio


async def coroutine_example():
    await asyncio.sleep(3)
    return "love you"


def CallBack(future):
    print("回调值:", future.result())


loop = asyncio.get_event_loop()
task = loop.create_task(coroutine_example())
print(task)
task.add_done_callback(CallBack)    # 两种方式获取回调值
print(task)
loop.run_until_complete(task)
print(task)
print(task.result())    # 两种方式获取回调值
loop.close()
