import asyncio

async def say_hello(name, delay):
    await asyncio.sleep(delay)
    print(name)

async def main():
    task1 = asyncio.create_task(say_hello("Alice", 1))

    await task1

asyncio.run(main())