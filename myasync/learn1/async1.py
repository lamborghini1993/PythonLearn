import asyncio


async def coroutine_example():
    await asyncio.sleep(3)
    print("Your are a good men!")

print("1")
coro = coroutine_example()
print("2", coro)
loop = asyncio.get_event_loop()
print("3")
loop.run_until_complete(coro)
print("4")
loop.close()
print("5")
